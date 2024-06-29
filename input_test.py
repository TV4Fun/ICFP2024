from icfp.decode import decode_message
from sys import argv

with open("test_inputs/" + argv[1]) as file:
    print(decode_message(file.read()))