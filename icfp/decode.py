from functools import partial
from typing import Callable, Optional

from .common import print_error, ICFP_CHARSET
from .encode import encode_string, encode_int

class Const:
    def __init__(self, name: str):
        self.name = name
        self.value: Optional[Callable] = None

    def __call__(self) -> object:
        if self.value is None:
            raise ValueError(f"Variable {self.name} is not defined")
        else:
            return self.value()

class OutOfScope:
    def __init__(self, name: str):
        self.name = name

    def __call__(self):
        raise ValueError(f"Attempt to evaluate out-of-scope variable {self.name}")

def decode_message(msg: str) -> str:
    tokens = tokenize(msg)
    idx, root = parse_token_tree(tokens, 0, {})
    if idx < len(tokens):
        print_error(f"Unexpected extra tokens: {tokens[idx:]}")
    return str(root())


def tokenize(msg: str) -> list[str]:
    return msg.split()


def parse_token_tree(tokens: list[str], idx: int, vs: dict[int, Callable]) -> tuple[int, Callable]:
    token = tokens[idx]
    idx_orig = idx
    n_args, vs, f = parse_token(token, vs)
    idx += 1
    args = []
    for _ in range(n_args):
        idx, arg = parse_token_tree(tokens, idx, vs)
        args.append(arg)
    if args:
        closure = partial(f, *args)
    else:
        closure = f
    closure.token = token
    closure.idx = idx_orig
    return idx, closure


def parse_token(token: str, vs: dict[int, Callable]) -> tuple[int, dict[int, Callable], Callable]:
    indicator = token[0]
    body = token[1:]

    if indicator == 'T' or indicator == 'F':
        if body:
            raise SyntaxError(f"Boolean token must have empty body. Found {body}")
        if indicator == 'T':
            return 0, vs, lambda: True
        else:
            return 0, vs, lambda: False
    elif indicator == 'I':
        return 0, vs, lambda *, s=body: decode_int(s)
    elif indicator == 'S':
        return 0, vs, lambda *, s=body: decode_string(s)
    elif indicator == 'U':
        if body == '-':
            return 1, vs, lambda i: -i()
        elif body == '!':
            return 1, vs, lambda x: not x()
        elif body == '#':
            return 1, vs, lambda s: decode_int(encode_string(s()))
        elif body == '$':
            return 1, vs, lambda n: decode_string(encode_int(n()))
        else:
            print_error(f"Unrecognized unary operator: {body}")
    elif indicator == 'B':
        if body == '+':
            def plus(x, y):
                x_val = x()
                y_val = y()
                return x_val + y_val
            return 2, vs, plus #lambda x, y: x() + y()
        elif body == '-':
            return 2, vs, lambda x, y: x() - y()
        elif body == '*':
            return 2, vs, lambda x, y,: x() * y()
        elif body == '/':
            return 2, vs, lambda x, y: int(x() / y())
        elif body == '%':
            def stupid_mod(x: Callable[[], int], y: Callable[[], int]) -> int:
                x_val = x()
                y_val = y()
                result = x_val % y_val
                if x_val < 0:
                    result -= y_val

                return result
            return 2, vs, stupid_mod
        elif body == '<':
            return 2, vs, lambda x, y: x() < y()
        elif body == '>':
            return 2, vs, lambda x, y: x() > y()
        elif body == '=':
            return 2, vs, lambda x, y: x() == y()
        elif body == '|':
            return 2, vs, lambda x, y: x() or y()
        elif body == '&':
            return 2, vs, lambda x, y: x() and y()
        elif body == '.':
            return 2, vs, lambda x, y: ''.join((x(), y()))
        elif body == 'T':
            return 2, vs, lambda x, y: y()[:x()]
        elif body == 'D':
            return 2, vs, lambda x, y: y()[x():]
        elif body == '$':
            return 2, vs, lambda f, x: f()(x)
        else:
            print_error(f"Unrecognized binary operator: {body}")
    elif indicator == '?':
        if body:
            print_error(f"? must have empty body. Found {body}")
        else:
            return 3, vs, lambda condition, yes, no: yes() if condition() else no()
    elif indicator == 'v':
        idx = decode_int(body)
        if idx in vs:
            return 0, vs, vs[idx]
        else:
            return 0, vs, OutOfScope(token)
    elif indicator == 'L':
        idx = decode_int(body)
        vs = vs.copy()
        arg = Const("v" + body)
        vs[idx] = arg

        def lambda_abstraction(f: Callable, *, arg=arg) -> Callable:
            def apply(arg_value: object) -> Callable:
                #arg_old_value = arg.value
                arg.value = arg_value
                result = f()
                #arg.value = arg_old_value
                return result
            return apply

        return 1, vs, lambda_abstraction
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
