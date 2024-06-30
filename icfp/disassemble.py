from typing import Generator

from .common import print_error
from .decode import tokenize, split_token, n_args

INDENT = ' ' * 4


def indent_message(msg: str) -> str:
    tokens = tokenize(msg)
    return '\n'.join(indent_token_tree(tokens))


def indent_token_tree(tokens: list[str], idx: int = 0, indent_level: int = 0) -> Generator[str, None, int]:
    is_root = idx == 0
    token = tokens[idx]
    yield INDENT * indent_level + token
    indicator, _ = split_token(token)
    num_args = n_args(indicator)
    idx += 1
    for _ in range(num_args):
        idx = yield from indent_token_tree(tokens, idx, indent_level + 1)

    if is_root and idx < len(tokens):
        print_error(f"Unexpected extra token(s): {tokens[idx:]}")

    return idx
