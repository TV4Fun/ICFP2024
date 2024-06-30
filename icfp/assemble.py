from re import compile

from . import decode, encode


TOKEN_REGEX = compile(r'#(.)\{([^}]*)}')


def assemble_message(msg: str) -> str:
    tokens = decode.tokenize(msg)
    return ' '.join(assemble_token(token) for token in tokens)


def assemble_token(token: str) -> str:
    if token.startswith("#"):
        match = TOKEN_REGEX.fullmatch(token)
        if not match:
            raise SyntaxError(f"Malformed assembler token: {token}")
        indicator = match.group(1)
        body = match.group(2)
        if indicator == 'S':
            return 'S' + encode.encode_string(body)
        elif indicator in {'I', 'L', 'v'}:
            return indicator + str(encode.encode_int(int(body)))
        else:
            raise SyntaxError(f"Unrecognized assembler token: {token}")
    else:
        return token
