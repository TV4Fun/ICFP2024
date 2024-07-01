from typing import Generator

from . import decode
from .common import print_error

INDENT = ' ' * 4


def indent_message(msg: str, disasm: bool = False) -> str:
    tokens = decode.tokenize(msg)
    return '\n'.join(indent_token_tree(tokens, disasm))


def indent_token_tree(tokens: list[str], disasm: bool, idx: int = 0, indent_level: int = 0) -> Generator[str, None, int]:
    is_root = idx == 0
    token = tokens[idx]
    if disasm:
        yield INDENT * indent_level + disassemble_token(token)
    else:
        yield INDENT * indent_level + token
    indicator, _ = decode.split_token(token)
    num_args = decode.n_args(indicator)
    idx += 1
    for _ in range(num_args):
        idx = yield from indent_token_tree(tokens, disasm, idx, indent_level + 1)

    if is_root and idx < len(tokens):
        print_error(f"Unexpected extra token(s): {tokens[idx:]}")

    return idx


def disassemble_token(token: str) -> str:
    indicator, body = decode.split_token(token)
    if indicator == 'S':
        return f'#S{{{decode.decode_string(body)}}}'
    if indicator in {'I', 'v', 'L'}:
        return f'#{indicator}{{{decode.decode_int(body)}}}'
    else:
        return token
