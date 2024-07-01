import requests
from sys import setrecursionlimit
from traceback import print_exc

from icfp.encode import encode_message
from icfp.decode import decode_message

setrecursionlimit(10000)

URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {"Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"}

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

    payload = encode_message(command)
    response = requests.post(URL, data=payload, headers=AUTH_HEADER)
    if print_raw:
        print(response.text)
    print(decode_message(response.text, decode_int))
