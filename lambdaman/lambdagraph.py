import numpy as np
import networkx as nx
from itertools import product

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
    possibilities = [[node[0] + 1, node[1]], [node[0], node[1] + 1], [node[0] - 1, node[1]], [node[0], node[1] - 1]]
    for option in possibilities:
        if any(coord < 0 for coord in option):
            continue
        if option[0] > lambda_map.shape[0] - 1 or option[1] > lambda_map.shape[1] - 1:
            continue
        neighbor = lambda_map[option[0]][option[1]]
        if not neighbor:
            neighbors.append(tuple(option))
    return neighbors

G = {lambda_man:find_neighbors(lambda_man)}

for node in nodes:
    neighbors = find_neighbors(node)
    if neighbors:
        G[node] = neighbors

G = nx.from_dict_of_lists(G)

H = nx.minimum_spanning_tree(G)
print(len(G.nodes))
print(lambda_man)

I = nx.complete_graph(H)
path = nx.approximation.traveling_salesman_problem(G, cycle=False)

print(path)
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


