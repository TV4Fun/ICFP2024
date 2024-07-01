from icfp.decode import decode_message
from sys import argv, setrecursionlimit

#setrecursionlimit(10000)

with open(argv[1]) as file:
    print(decode_message(file.read()))