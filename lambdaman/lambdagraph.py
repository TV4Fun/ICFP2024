from icfp.encode import encode_digit, encode_char
from icfp.decode import decode_int
import networkx as nx
import numpy as np
from math import log


map_file = "lambdaman5.txt"

with open(map_file) as f:
    lines = f.read().splitlines()

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == "L":
            lambda_man = (row, col)
            break
    else:
        continue
    break
lambda_map = np.array([[c == "#" for c in line] for line in lines], dtype=np.bool)

nodes = [(int(x), int(y)) for x, y in zip(*np.nonzero(np.logical_not(lambda_map)))]


def find_neighbors(node):
    neighbors = []
    x, y = node
    possibilities = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    for row, col in possibilities:
        if 0 <= row < lambda_map.shape[0] and 0 <= col < lambda_map.shape[1]:
            neighbor = lambda_map[row, col]
            if not neighbor:
                neighbors.append((row, col))
    return neighbors


G = {lambda_man: find_neighbors(lambda_man)}

for node in nodes:
    neighbors = find_neighbors(node)
    if neighbors:
        G[node] = neighbors

G = nx.from_dict_of_lists(G)

H = nx.minimum_spanning_tree(G)


I = nx.complete_graph(H)
path = nx.approximation.traveling_salesman_problem(G, cycle=False)



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


