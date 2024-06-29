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


def heuristic(
    state: State,
    targets: Set[Tuple[int, int]],
    target_grid: Dict[Tuple[int, int], Set[Tuple[int, int]]],
) -> int:
    if not targets:
        return 0

    grid_key = (state.x // 100, state.y // 100)
    nearby_targets = target_grid.get(grid_key, set())
    if not nearby_targets:
        nearby_targets = targets

    return min(manhattan_distance(state.x, state.y, x, y) for x, y in nearby_targets)


def create_target_grid(
    targets: Set[Tuple[int, int]], grid_size: int = 100
) -> Dict[Tuple[int, int], Set[Tuple[int, int]]]:
    grid = defaultdict(set)
    for x, y in targets:
        grid_key = (x // grid_size, y // grid_size)
        grid[grid_key].add((x, y))
    return grid


def solve_maze(coordinates: Set[Tuple[int, int]]) -> str:
    start = State(0, 0, 0, 0)
    targets = coordinates.copy()
    target_grid = create_target_grid(targets)

    pq = [(0, 0, start, "")]
    visited = set()
    g_scores = defaultdict(lambda: float("inf"))
    g_scores[start] = 0

    while pq:
        _, cost, state, path = heapq.heappop(pq)

        if (state.x, state.y) in targets:
            targets.remove((state.x, state.y))
            grid_key = (state.x // 100, state.y // 100)
            target_grid[grid_key].remove((state.x, state.y))
            if not target_grid[grid_key]:
                del target_grid[grid_key]
            if not targets:
                return path

        if state in visited:
            continue
        visited.add(state)

        for action, (dvx, dvy) in CONTROLS.items():
            new_vx, new_vy = state.vx + dvx, state.vy + dvy
            new_x, new_y = state.x + new_vx, state.y + new_vy
            new_state = State(new_x, new_y, new_vx, new_vy)

            new_cost = cost + 1
            if new_cost < g_scores[new_state]:
                g_scores[new_state] = new_cost
                f_score = new_cost + heuristic(new_state, targets, target_grid)
                heapq.heappush(pq, (f_score, new_cost, new_state, path + str(action)))

    return "No solution found"


def get_optimal_path(input_str: str) -> str:
    try:
        coordinates = parse_input(input_str)
        return solve_maze(coordinates)
    except Exception as e:
        print(f"Error in get_optimal_path: {str(e)}")
        return "Error: Unable to find optimal path"
