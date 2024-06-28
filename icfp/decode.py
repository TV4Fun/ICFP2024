from .util import format_error

ICFP_CHARSET = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n"""


def decode_message(msg: str) -> str:
    tokens = tokenize(msg)
    return ''.join(str(decode_token(token)) for token in tokens)


def tokenize(msg: str) -> list[str]:
    return msg.split()


def decode_token(token: str):
    indicator = token[0]
    body = token[1:]

    if indicator == 'T' or indicator == 'F':
        if body:
            raise SyntaxError(f"Boolean token must have empty body. Found {body}")
        return True if indicator == 'T' else False
    elif indicator == 'I':
        return decode_int(body)
    elif indicator == 'S':
        return decode_string(body)
    else:
        return format_error(f"Unsupported token type: {token}")


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

