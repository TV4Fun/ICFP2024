import math
from typing import List, Tuple, Dict
import heapq

# Define the keypad controls and their effects on velocity
CONTROLS = {
    7: (-1, 1),
    8: (0, 1),
    9: (1, 1),
    4: (-1, 0),
    5: (0, 0),
    6: (1, 0),
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
}


def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def reconstruct_path(came_from: Dict, current: Tuple) -> List[int]:
    path = []
    while current in came_from:
        current, action = came_from[current]
        path.append(action)
    return path[::-1]


def prim_mst(coordinates: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    num_points = len(coordinates)
    if num_points == 0:
        return []

    mst_edges = []
    in_mst = [False] * num_points
    edge_heap = []

    def add_edges(point_index: int):
        in_mst[point_index] = True
        for i in range(num_points):
            if not in_mst[i]:
                distance = manhattan_distance(coordinates[point_index], coordinates[i])
                heapq.heappush(edge_heap, (distance, point_index, i))

    add_edges(0)

    while edge_heap and len(mst_edges) < num_points - 1:
        distance, u, v = heapq.heappop(edge_heap)
        if not in_mst[v]:
            mst_edges.append((u, v))
            add_edges(v)

    return mst_edges


def get_mst_order(
    coordinates: List[Tuple[int, int]], mst_edges: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    from collections import defaultdict

    neighbors = defaultdict(list)
    for u, v in mst_edges:
        neighbors[u].append(v)
        neighbors[v].append(u)

    visited = set()
    order = []

    def dfs(node):
        order.append(node)
        visited.add(node)
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(0)
    return [coordinates[i] for i in order]


def navigate(coordinates: List[Tuple[int, int]]) -> str:
    # Include the starting point (0, 0)
    coordinates = [(0, 0)] + coordinates
    mst_edges = prim_mst(coordinates)
    ordered_coordinates = get_mst_order(coordinates, mst_edges)

    full_path = []
    start = (0, 0, 0, 0)  # (x, y, vx, vy)

    for target in ordered_coordinates[1:]:  # Skip the starting point itself
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: manhattan_distance(start[:2], target)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current[:2] == target:
                path = reconstruct_path(came_from, current)
                full_path.extend(path)
                start = current
                break

            for action, (dvx, dvy) in CONTROLS.items():
                x, y, vx, vy = current
                new_vx, new_vy = vx + dvx, vy + dvy
                new_x, new_y = x + new_vx, y + new_vy
                neighbor = (new_x, new_y, new_vx, new_vy)

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = (current, action)
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + manhattan_distance(
                        (new_x, new_y), target
                    )
                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return "".join(map(str, full_path))


def parse_input(input_str: str) -> List[Tuple[int, int]]:
    coordinates = []
    for line in input_str.strip().split("\n"):
        x, y = map(int, line.split())
        coordinates.append((x, y))
    return coordinates


def get_optimal_path(input_str: str) -> str:
    coordinates = parse_input(input_str)
    return navigate(coordinates)
