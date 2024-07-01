from functools import partial, cache
from typing import Callable, Protocol, TypeVar

from . import disassemble, encode
from .common import print_error, ICFP_CHARSET
from .frozen_dict import FrozenDict

T = TypeVar('T', int, str, bool, 'Function', covariant=True)


class Function(Protocol[T]):
    token: str
    idx: int

    def __call__(self, vals: FrozenDict[int, 'Function']) -> T:
        ...


class IncompleteFunction(Protocol[T]):
    def __call__(self, *args: Function, vals: FrozenDict[int, 'Function']) -> T:
        ...


ValDict = FrozenDict[int, Function]


def decode_message(msg: str, read_int: bool = False) -> str:
    tokens = tokenize(msg)
    idx, root = parse_token_tree(tokens, 0)
    if idx < len(tokens):
        print_error(f"Unexpected extra tokens: {tokens[idx:]}")

    decoded_msg = root(vals=FrozenDict())
    if read_int:
        return str(decode_int(encode.encode_string(decoded_msg.split()[0])))
    else:
        return str(decoded_msg)


def tokenize(msg: str) -> list[str]:
    return msg.split()


def parse_token_tree(tokens: list[str], idx: int) -> tuple[int, Function]:
    token = tokens[idx]
    idx_orig = idx
    n_args, f = parse_token(token)
    idx += 1
    args = []
    for _ in range(n_args):
        idx, arg = parse_token_tree(tokens, idx)
        args.append(arg)
    if args:
        closure = partial(f, *args)
    else:
        closure = f
    closure = cache(closure)
    closure.token = disassemble.disassemble_token(token)
    closure.idx = idx_orig
    return idx, closure


def parse_token(token: str) -> tuple[int, Callable]:
    indicator, body = split_token(token)

    if indicator == 'T' or indicator == 'F':
        if body:
            raise SyntaxError(f"Boolean token must have empty body. Found {body}")
        if indicator == 'T':
            return 0, lambda *, vals: True
        else:
            return 0, lambda *, vals: False
    elif indicator == 'I':
        return 0, lambda *, vals, s=body: decode_int(s)
    elif indicator == 'S':
        return 0, lambda *, vals, s=body: decode_string(s)
    elif indicator == 'U':
        if body == '-':
            return 1, lambda i, *, vals: -i(vals=vals)
        elif body == '!':
            return 1, lambda x, *, vals: not x(vals=vals)
        elif body == '#':
            return 1, lambda s, *, vals: decode_int(encode.encode_string(s(vals=vals)))
        elif body == '$':
            return 1, lambda n, *, vals: decode_string(encode.encode_int(n(vals=vals)))
        else:
            print_error(f"Unrecognized unary operator: {body}")
    elif indicator == 'B':
        if body == '+':
            return 2, lambda x, y, *, vals: x(vals=vals) + y(vals=vals)
        elif body == '-':
            return 2, lambda x, y, *, vals: x(vals=vals) - y(vals=vals)
        elif body == '*':
            return 2, lambda x, y, *, vals: x(vals=vals) * y(vals=vals)
        elif body == '/':
            def truncated_divide(x: Function[int], y: Function[int], *, vals: ValDict) -> int:
                quotient, remainder = divmod(x(vals=vals), y(vals=vals))
                if remainder and quotient < 0:
                    quotient += 1
                return quotient

            return 2, truncated_divide
        elif body == '%':
            def stupid_mod(x: Function[int], y: Function[int], *, vals: ValDict) -> int:
                x_val = x(vals=vals)
                y_val = y(vals=vals)
                result = x_val % y_val
                if x_val < 0:
                    result -= y_val

                return result

            return 2, stupid_mod
        elif body == '<':
            return 2, lambda x, y, *, vals: x(vals=vals) < y(vals=vals)
        elif body == '>':
            return 2, lambda x, y, *, vals: x(vals=vals) > y(vals=vals)
        elif body == '=':
            return 2, lambda x, y, *, vals: x(vals=vals) == y(vals=vals)
        elif body == '|':
            return 2, lambda x, y, *, vals: x(vals=vals) or y(vals=vals)
        elif body == '&':
            return 2, lambda x, y, *, vals: x(vals=vals) and y(vals=vals)
        elif body == '.':
            return 2, lambda x, y, *, vals: ''.join((x(vals=vals), y(vals=vals)))
        elif body == 'T':
            return 2, lambda x, y, *, vals: y(vals=vals)[:x(vals=vals)]
        elif body == 'D':
            return 2, lambda x, y, *, vals: y(vals=vals)[x(vals=vals):]
        elif body == '$':
            return 2, lambda f, x, *, vals: f(vals=vals)(transfer_debug_info(x, partial(x, vals=vals)))
        else:
            print_error(f"Unrecognized binary operator: {body}")
    elif indicator == '?':
        if body:
            print_error(f"? must have empty body. Found {body}")
        else:
            return 3, lambda condition, yes, no, *, vals: yes(vals=vals) if condition(vals=vals) else no(vals=vals)
    elif indicator == 'v':
        v_idx = decode_int(body)
        return 0, lambda *, vals, idx=v_idx: vals[idx]()

    elif indicator == 'L':
        idx = decode_int(body)

        def lambda_abstraction(f: Function, *, vals: ValDict) -> Callable:
            def apply(arg_value: Function, *, idx=idx) -> Callable:
                result = f(vals=vals + (idx, arg_value))
                return result

            return apply

        return 1, lambda_abstraction
    else:
        raise SyntaxError(f"Unrecognized indicator: {indicator}")


def split_token(token: str) -> tuple[str, str]:
    return token[0], token[1:]


def n_args(indicator: str) -> int:
    if indicator in {'T', 'F', 'I', 'S', 'v'}:
        return 0
    elif indicator in {'U', 'L'}:
        return 1
    elif indicator == 'B':
        return 2
    elif indicator == '?':
        return 3
    else:
        raise SyntaxError(f"Unrecognized indicator: {indicator}")


def decode_int(body: str) -> int:
    result = 0
    for digit in body:
        result *= 94
        result += decode_digit(digit)
    return result


def decode_digit(digit: str) -> int:
    return ord(digit) - ord('!')


def decode_string(body: str) -> str:
    return ''.join(decode_char(char) for char in body)


def decode_char(char: str) -> str:
    o = ord(char) - ord('!')
    return ICFP_CHARSET[o]


def transfer_debug_info(from_fn: Function, to_fn: Callable) -> Function:
    to_fn.idx = from_fn.idx
    to_fn.token = from_fn.token
    return to_fn
