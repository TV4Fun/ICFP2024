from icfp.encode import encode_message
from sys import argv

with open("test_outputs/" + argv[1]) as file:
    print(encode_message(file.read()))