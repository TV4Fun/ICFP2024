from sys import argv

from icfp.disassemble import indent_message

with open(argv[1]) as file:
    message = file.read()

message = indent_message(message)

with open(argv[1], 'w') as file:
    file.write(message)
    file.write('\n')
