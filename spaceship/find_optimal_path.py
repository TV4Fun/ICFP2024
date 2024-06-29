import math
from typing import List, Tuple
import heapq
import requests
from collections import defaultdict

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


def reconstruct_path(came_from: dict, current: Tuple) -> List[int]:
    path = []
    while current in came_from:
        current, action = came_from[current]
        path.append(action)
    return path[::-1]


def nearest_neighbor_tsp(coordinates: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not coordinates:
        return []

    unvisited = set(range(len(coordinates)))
    current_index = 0
    tour = [coordinates[current_index]]
    unvisited.remove(current_index)

    while unvisited:
        nearest_index = min(
            unvisited,
            key=lambda idx: manhattan_distance(
                coordinates[current_index], coordinates[idx]
            ),
        )
        tour.append(coordinates[nearest_index])
        unvisited.remove(nearest_index)
        current_index = nearest_index

    return tour


def navigate(coordinates: List[Tuple[int, int]]) -> str:
    coordinates = [(0, 0)] + coordinates
    ordered_coordinates = nearest_neighbor_tsp(coordinates)

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
