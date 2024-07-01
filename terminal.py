import requests
from sys import setrecursionlimit, argv
from traceback import print_exc

from icfp.encode import encode_message
from icfp.decode import decode_message

setrecursionlimit(10000)

URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {"Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"}


def send_command(command: str) -> str:
    payload = encode_message(command)
    response = requests.post(URL, data=payload, headers=AUTH_HEADER)
    return response.text


if len(argv) > 1:
    with open(argv[1], "r") as f:
        response = send_command(f.read())
    print(decode_message(response))
    exit(0)

while True:
    command = input("> ")
    if not command:
        continue

    print_raw = False
    decode_int = False
    while command[0] in {"!", "#"}:
        if command.startswith('!'):
            print_raw = True
        elif command.startswith('#'):
            decode_int = True
        command = command[1:]

    response = send_command(command)
    if print_raw:
        print(response)
    else:
        print(decode_message(response, decode_int))
