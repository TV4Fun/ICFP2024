import networkx as nx
import numpy as np

"""
'U': {8, 9, 10, 11, 12, 13, 14, 15}
'D': {4, 5, 6, 7, 12, 13, 14, 15}
'L': {2, 3, 6, 7, 10, 11, 14, 15}
'R': {1, 3, 5, 7, 9, 11, 13, 15}
"""

WAYS = {
    1: "R",
    2: "L",
    3: "LR",
    4: "D",
    5: "DR",
    6: "LD",
    7: "LDR",
    8: "U",
    9: "UR",
    10: "LU",
    11: "LUR",
    12: "UD",
    13: "UDR",
    14: "LUD",
    15: "LUDR"
}

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


class LambdaMap:
    def __init__(self, map_file: str):
        self.map, self.origin = create_array(map_file)
        self.pills = [(int(x), int(y)) for x, y in zip(*np.nonzero(self.map)) if (int(x), int(y))]
        self.max_distance = 1
        self.origin_paths, self.origin_distances = self.walk()
        self.graph = self.create_graph()

    def walk(self) -> tuple[dict[tuple[int, int], str], dict[tuple[int, int], int]]:
        distances = dict(zip(self.pills, ["K" for _ in self.pills]))
        ways = WAYS[self.map[self.origin]]
        distances[self.origin] = ""
        visited = [self.origin]
        for way in ways:
            coord = (DIRECTIONS[way][0] + self.origin[0], DIRECTIONS[way][1] + self.origin[1])
            distances[coord] = way
            visited.append(coord)

        while any(distance == "K" for distance in distances.values()):
            queue = [coord for coord in visited if len(distances[coord]) == self.max_distance and distances[coord] != "K"]
            while queue:
                coord = queue.pop()
                path = distances[coord]
                ways = WAYS[self.map[coord]]
                for way in ways:
                    coords = (DIRECTIONS[way][0] + coord[0], DIRECTIONS[way][1] + coord[1])
                    if distances[coords] == "K":
                        new_path = path + way
                        distances[coords] = new_path
                        self.max_distance = len(new_path)
                        visited.append(coords)

        abs_distances = dict(zip(list(distances.keys()), [len(distances[key]) for key in list(distances.keys())]))
        return distances, abs_distances

    def lazy_path(self) -> str:
        paths = sorted(list(self.origin_paths.values()), key=lambda x: len(x), reverse=True)
        combined_paths = []

        while paths:
            path = paths.pop()
            if not any(other_path.startswith(path) for other_path in paths):
                combined_paths.append(path)

        full_path = ""
        if len(combined_paths) > 1:
            for path in combined_paths:
                reverse_path = path[::-1].translate(str.maketrans("UDLR", "DURL"))
                full_path += path + reverse_path
        else:
            full_path = combined_paths[0]

        return full_path

    def create_graph(self) -> nx.MultiGraph:
        G = nx.MultiGraph()
        G.add_nodes_from(self.pills)
        for node in G:
            edges = WAYS[self.map[node]]
            coords = [(DIRECTIONS[way][0] + node[0], DIRECTIONS[way][1] + node[1]) for way in edges]
            for coord in coords:
                G.add_edge(node, coord)
        return G

    def lazy_tsp(self) -> str:
        lazy_tsp = nx.approximation.traveling_salesman_problem(self.graph, cycle=False)
        origin = lazy_tsp.index(self.origin)
        first_path = lazy_tsp[:origin]
        back_path = [self.origin] + first_path[::-1] + first_path[1:] + lazy_tsp[origin:]

        return stringify(back_path)


def create_array(map_file: str) -> tuple[np.array, tuple[int, int]]:
    with open(map_file) as f:
        lines = f.read().splitlines()
    map_shape = (len(lines), len(lines[0]))
    map_array = np.full(map_shape, 0b1111, dtype=int)
    lambda_man = (0, 0)

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if row == 0:
                map_array[row, col] &= 0b0111
            if row == len(lines) - 1:
                map_array[row, col] &= 0b1011
            if col == 0:
                map_array[row, col] &= 0b1101
            if col == len(lines[0]) - 1:
                map_array[row, col] &= 0b1110

            if char == "L":
                lambda_man = (row, col)
            elif char == "#":
                # U
                if row < map_shape[0] - 1:
                    map_array[row + 1, col] &= 0b0111
                # D
                if row > 0:
                    map_array[row - 1, col] &= 0b1011
                # L
                if col < map_shape[1] - 1:
                    map_array[row, col + 1] &= 0b1101
                # R
                if col > 0:
                    map_array[row, col - 1] &= 0b1110

                map_array[row, col] = 0b0000

    return map_array, lambda_man


def stringify(path: list[tuple[int, int]]) -> str:
    nodes = path

    origin = nodes.pop(0)
    stringified = ""
    while nodes:
        next = nodes.pop(0)
        if origin[0] - next[0] == 1:
            stringified += "U"
        elif origin[0] - next[0] == -1:
            stringified += "D"
        elif origin[1] - next[1] == 1:
            stringified += "L"
        elif origin[1] - next[1] == -1:
            stringified += "R"
        origin = next

    return stringified
