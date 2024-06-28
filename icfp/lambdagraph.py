import numpy as np
import networkx as nx

lambda_map = """
L...#.
#.#.#.
##....
...###
.##..#
....##
"""

lambda_map = lambda_map.split("\n")
lambda_map = [[c for c in line] for line in lambda_map if line]
lambda_map = np.array(lambda_map)
print(lambda_map)

lambda_man = np.where(lambda_map == "L")
lambda_man = (int(lambda_man[0][0]), int(lambda_man[1][0]))


def find_neighbors(node):
    neighbors = []
    possibilities = [[node[0] + 1, node[1]], [node[0], node[1] + 1], [node[0] - 1, node[1]], [node[0], node[1] - 1]]
    for option in possibilities:
        if any(coord < 0 for coord in option):
            continue
        if option[0] > lambda_map.shape[0] - 1 or option[1] > lambda_map.shape[1] - 1:
            continue

        neighbor = lambda_map[option[0]][option[1]]
        if neighbor == ".":
            neighbors.append(tuple(option))
    return neighbors

nodes = [(int(x), int(y)) for x, y in zip(np.where(lambda_map == ".")[0], np.where(lambda_map == ".")[1])]
root_neighbors = find_neighbors(lambda_man)
G = {lambda_man: root_neighbors}
for node in nodes:
    neighbors = find_neighbors(node)
    G[node] = neighbors

G = nx.from_dict_of_lists(G)
H = nx.approximation.traveling_salesman_problem(G, cycle=False)

def stringify(path):
    nodes = path
    origin = nodes.pop()
    string = ""
    while nodes:
        next = H.pop()
        if origin[0] - next[0] == 1:
            string += "R"
        elif origin[0] - next[0] == -1:
            string += "L"
        elif origin[1] - next[1] == 1:
            string += "U"
        else:
            string += "D"
        origin = next

    return string
print(stringify(H))