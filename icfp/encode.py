from .decode import ICFP_CHARSET


ENCODER = {char: code for code, char in enumerate(ICFP_CHARSET)}


def encode_string(msg: str) -> str:
    tokens = []
    chars = []
    raw = False
    for char in msg:
        if char == '{':
            if chars:
                if tokens:
                    last_token = tokens.pop()
                    tokens.append("B.")
                    tokens.append(last_token)
                tokens.append('S' + ''.join(encode_char(char) for char in chars))
                chars = []
            raw = True
        elif char == '}':
            if chars:
                if tokens:
                    last_token = tokens.pop()
                    tokens.append("B.")
                    tokens.append(last_token)
                tokens.append(''.join(chars))
                chars = []
            raw = False
        else:
            chars.append(char)
    if chars:
        if tokens:
            last_token = tokens.pop()
            tokens.append("B.")
            tokens.append(last_token)
        if raw:
            tokens.append(''.join(chars))
        else:
            tokens.append('S' + ''.join(encode_char(char) for char in chars))

    return ' '.join(tokens)


def encode_int(value: int) -> str:
    digits_reversed: list[str] = []

    while value > 0:
        digits_reversed.append(encode_digit(value % 94))
        value //= 94

    return 'I' + ''.join(reversed(digits_reversed))


def encode_digit(digit: int) -> str:
    return chr(digit + ord('!'))


def encode_char(char: str) -> str:
    o = ENCODER[char]
    return chr(o + ord('!'))