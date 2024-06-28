import requests
from traceback import print_exc

from icfp.encode import encode_string
from icfp.decode import decode_message


URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {
    "Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"
}

while True:
    try:
        command = input("> ")
        if not command:
            continue
        payload = encode_string(command)
        response = requests.post(URL, data=payload, headers=AUTH_HEADER)
        print(decode_message(response.text))
    except (KeyboardInterrupt, EOFError):
        exit(0)
    except:
        print_exc()