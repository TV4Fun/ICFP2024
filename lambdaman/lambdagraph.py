# import networkx as nx
import numpy as np

"""
'U': {8, 9, 10, 11, 12, 13, 14, 15}
'D': {4, 5, 6, 7, 12, 13, 14, 15}
'L': {2, 3, 6, 7, 10, 11, 14, 15}
'R': {1, 3, 5, 7, 9, 11, 13, 15}
"""

WAYS = {
    "U": {0b1000, 0b1001, 0b1010, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111},
    "D": {0b0100, 0b0101, 0b0110, 0b0111, 0b1100, 0b1101, 0b1110, 0b1111},
    "L": {0b0010, 0b0011, 0b0110, 0b0111, 0b1010, 0b1011, 0b1110, 0b1111},
    "R": {0b0001, 0b0011, 0b0101, 0b0111, 0b1001, 0b1011, 0b1101, 0b1111},
}


def create_array(map_file: str) -> tuple[np.array, tuple[int, int]]:
    with open(map_file) as f:
        lines = f.read().splitlines()
    map_shape = (len(lines), len(lines[0]))
    map_array = np.full(map_shape, 0b1111)
    lambda_man = (0, 0)

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "L":
                lambda_man = (row, col)
            elif char == "#":
                print(char)
                print(row, col)
                # U
                if row > 0:
                    map_array[row - 1, col] &= 0b0111
                # D
                if row < map_shape[0] - 1:
                    map_array[row - 1, col] &= 0b1011
                # L
                if col > 0:
                    map_array[row, col - 1] &= 0b1101
                # R
                if col < map_shape[1] - 1:
                    map_array[row, col + 1] &= 0b1110

                map_array[row, col] = 0b0000

    return map_array, lambda_man


def stringify(path):
    nodes = path

    origin = nodes.pop()
    string = ""
    while nodes:
        next = nodes.pop(0)
        if origin[0] - next[0] == 1:
            string += "U"
        elif origin[0] - next[0] == -1:
            string += "D"
        elif origin[1] - next[1] == 1:
            string += "L"
        else:
            string += "R"
        origin = next

    return string