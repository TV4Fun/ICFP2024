import requests
from traceback import print_exc

from icfp.encode import encode_and_compile
from icfp.decode import decode_message


URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {"Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"}

while True:
    command = input("> ")
    if not command:
        continue
    payload = encode_and_compile(command)
    response = requests.post(URL, data=payload, headers=AUTH_HEADER)
    # print(response.text)
    print(decode_message(response.text))
