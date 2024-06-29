from typing import List, Tuple, Dict, NamedTuple, Set
from collections import defaultdict
import heapq

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


class State(NamedTuple):
    x: int
    y: int
    vx: int
    vy: int


def parse_input(input_str: str) -> Set[Tuple[int, int]]:
    coordinates = set()
    for line in input_str.strip().split("\n"):
        try:
            x, y = map(int, line.split())
            coordinates.add((x, y))
        except ValueError as e:
            print(f"Error parsing line: {line}")
            print(f"Error message: {str(e)}")
            continue

    if not coordinates:
        raise ValueError("No valid coordinates found in the input")

    return coordinates


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def navigate(coordinates: Set[Tuple[int, int]]) -> str:
    state = State(0, 0, 0, 0)
    nav_plan = []

    while coordinates:
        min_distance = float("inf")
        best_command = None
        best_coord = None

        for command, (dvx, dvy) in CONTROLS.items():
            new_state = State(
                state.x + state.vx + dvx,
                state.y + state.vy + dvy,
                state.vx + dvx,
                state.vy + dvy,
            )

            for coord in coordinates:
                distance = manhattan_distance(
                    new_state.x, new_state.y, coord[0], coord[1]
                )
                if distance < min_distance:
                    min_distance = distance
                    best_command = command
                    best_coord = coord

        if best_command is None:
            break

        nav_plan.append(str(best_command))
        state = State(
            state.x + state.vx + CONTROLS[best_command][0],
            state.y + state.vy + CONTROLS[best_command][1],
            state.vx + CONTROLS[best_command][0],
            state.vy + CONTROLS[best_command][1],
        )
        coordinates.remove(best_coord)

    return "".join(nav_plan)


# Example usage
input_str = """
1 1
1 0
1 -1
0 -1
0 1
-1 1
-1 0
-1 -1
"""

coordinates = parse_input(input_str)
nav_plan = navigate(coordinates)
print("Navigation plan:", nav_plan)
