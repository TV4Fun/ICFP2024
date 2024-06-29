from functools import partial
from typing import Callable

from .common import print_error, ICFP_CHARSET
from .encode import encode_string, encode_int


def decode_message(msg: str) -> str:
    tokens = tokenize(msg)
    idx, root = parse_token_tree(tokens, 0)
    if idx < len(tokens):
        print_error(f"Unexpected extra tokens: {tokens[idx:]}")
    return str(root())


def tokenize(msg: str) -> list[str]:
    return msg.split()


def parse_token_tree(tokens: list[str], idx: int) -> tuple[int, Callable]:
    token = tokens[idx]
    idx_orig = idx
    n_args, f = parse_token(token)
    idx += 1
    args = []
    for _ in range(n_args):
        idx, arg = parse_token_tree(tokens, idx)
        args.append(arg)
    closure = partial(f, *args)
    closure.token = token
    closure.idx = idx_orig
    return idx, closure


def parse_token(token: str) -> tuple[int, Callable]:
    indicator = token[0]
    body = token[1:]

    if indicator == 'T' or indicator == 'F':
        if body:
            raise SyntaxError(f"Boolean token must have empty body. Found {body}")
        if indicator == 'T':
            return 0, lambda **kwargs: True
        else:
            return 0, lambda **kwargs: False
    elif indicator == 'I':
        return 0, lambda *, s=body, **kwargs: decode_int(s)
    elif indicator == 'S':
        return 0, lambda *, s=body, **kwargs: decode_string(s)
    elif indicator == 'U':
        if body == '-':
            return 1, lambda i, **kwargs: -i(**kwargs)
        elif body == '!':
            return 1, lambda x, **kwargs: not x(**kwargs)
        elif body == '#':
            return 1, lambda s, **kwargs: decode_int(encode_string(s(**kwargs)))
        elif body == '$':
            return 1, lambda n, **kwargs: decode_string(encode_int(n(**kwargs)))
        else:
            print_error(f"Unrecognized unary operator: {body}")
    elif indicator == 'B':
        if body == '+':
            return 2, lambda x, y, **kwargs: x(**kwargs) + y(**kwargs)
        elif body == '-':
            return 2, lambda x, y, **kwargs: x(**kwargs) - y(**kwargs)
        elif body == '*':
            return 2, lambda x, y, **kwargs: x(**kwargs) * y(**kwargs)
        elif body == '/':
            return 2, lambda x, y, **kwargs: int(x(**kwargs) / y(**kwargs))
        elif body == '%':
            def stupid_mod(x, y, **kwargs):
                x_val = x(**kwargs)
                y_val = y(**kwargs)
                result = x_val % y_val
                if x_val < 0:
                    result -= y_val

                return result
            return 2, stupid_mod
        elif body == '<':
            return 2, lambda x, y, **kwargs: x(**kwargs) < y(**kwargs)
        elif body == '>':
            return 2, lambda x, y, **kwargs: x(**kwargs) > y(**kwargs)
        elif body == '=':
            return 2, lambda x, y, **kwargs: x(**kwargs) == y(**kwargs)
        elif body == '|':
            return 2, lambda x, y, **kwargs: x(**kwargs) or y(**kwargs)
        elif body == '&':
            return 2, lambda x, y, **kwargs: x(**kwargs) and y(**kwargs)
        elif body == '.':
            return 2, lambda x, y, **kwargs: ''.join((x(**kwargs), y(**kwargs)))
        elif body == 'T':
            return 2, lambda x, y, **kwargs: y(**kwargs)[:x(**kwargs)]
        elif body == 'D':
            return 2, lambda x, y, **kwargs: y(**kwargs)[x(**kwargs):]
        elif body == '$':
            return 2, lambda f, x, **kwargs: f(**kwargs)(x, **kwargs)
        else:
            print_error(f"Unrecognized binary operator: {body}")
    elif indicator == '?':
        if body:
            print_error(f"? must have empty body. Found {body}")
        else:
            return 3, lambda condition, yes, no, **kwargs: yes(**kwargs) if condition(**kwargs) else no(**kwargs)
    elif indicator == 'v':
        v_idx = decode_int(body)
        return 0, lambda *, vs, idx=v_idx, **kwargs: vs[idx](vs=vs, **kwargs)
    elif indicator == 'L':
        v_idx = decode_int(body)

        def lambda_abstraction(f, *, vs={}, idx=v_idx, **kwargs):
            def apply(arg, *, vs=vs):
                vs = vs.copy()
                vs[idx] = arg
                return f(vs=vs)

            return apply

        return 1, lambda_abstraction
    else:
        print_error(f"Unsupported token type: {token}")


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
