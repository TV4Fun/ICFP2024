import sys
import os
from pathlib import Path
import requests
from traceback import print_exc
import time
from typing import List, Tuple

# Add the parent directory to the Python path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from icfp.encode import encode_message
from icfp.decode import decode_message

URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {"Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"}


class SpaceshipPathfinder:
    def __init__(self):
        self.directions = {
            1: (-1, -1),
            2: (0, -1),
            3: (1, -1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, 1),
            8: (0, 1),
            9: (1, 1),
        }

    def find_path(self, targets: List[Tuple[int, int]]) -> str:
        first_move = self.find_nearest_point(targets)
        ordered_targets = self.nearest_neighbor_tsp(first_move, targets)
        path = self.generate_path(ordered_targets)
        return path

    def find_nearest_point(self, targets: List[Tuple[int, int]]) -> Tuple[int, int]:
        return min(targets, key=lambda x: max(abs(x[0]), abs(x[1])))

    def nearest_neighbor_tsp(
        self, start: Tuple[int, int], targets: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        unvisited = set(targets)
        path = [start]
        unvisited.remove(start)

        while unvisited:
            current = path[-1]
            next_target = min(
                unvisited, key=lambda x: self.manhattan_distance(current, x)
            )
            path.append(next_target)
            unvisited.remove(next_target)

        return path

    def manhattan_distance(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def generate_path(self, ordered_targets: List[Tuple[int, int]]) -> str:
        path = []
        current_pos = (0, 0)
        vx, vy = 0, 0

        for target in ordered_targets:
            while current_pos != target:
                dx = target[0] - current_pos[0]
                dy = target[1] - current_pos[1]

                move_x = max(min(dx - vx, 1), -1)
                move_y = max(min(dy - vy, 1), -1)

                move = next(
                    key
                    for key, value in self.directions.items()
                    if value == (move_x, move_y)
                )
                path.append(str(move))

                vx += move_x
                vy += move_y
                current_pos = (current_pos[0] + vx, current_pos[1] + vy)

        return "".join(path)

    @staticmethod
    def parse_coordinates(coordinate_list: str) -> List[Tuple[int, int]]:
        return [
            tuple(map(int, line.strip().split()))
            for line in coordinate_list.strip().split("\n")
        ]


def send_command(command: str) -> str:
    payload = encode_message(command)
    response = requests.post(URL, data=payload, headers=AUTH_HEADER)
    return decode_message(response.text)


def get_spaceship_coordinates(ship_number: int) -> str:
    return send_command(f"get spaceship{ship_number}")


def solve_spaceship(ship_number: int, path: str) -> str:
    return send_command(f"solve spaceship{ship_number} {path}")


def main():
    pathfinder = SpaceshipPathfinder()

    for ship_number in range(1, 26):  # 1 to 25
        try:
            # Get coordinates for the current spaceship
            coordinates_str = get_spaceship_coordinates(ship_number)

            # Parse coordinates
            coordinates = pathfinder.parse_coordinates(coordinates_str)

            # Find the optimal path
            optimal_path = pathfinder.find_path(coordinates)

            # Send the solution to the terminal
            result = solve_spaceship(ship_number, optimal_path)

            # Print results
            print(f"Spaceship {ship_number}:")
            print(f"Path length: {len(optimal_path)}")
            print(f"Result: {result}")
            print("Correct" if result.startswith("Correct") else "Incorrect")
            print()

            # Add a small delay to avoid overwhelming the server
            time.sleep(1)
        except Exception as e:
            print(f"Error processing spaceship{ship_number}: {str(e)}")
            print_exc()
            print()


if __name__ == "__main__":
    main()

"""
SPACESHIP SOLUTIONS:
1 - 5, correct, best achieved
2 - 55
3 - 13  
4 - 105 
5 - 213 
6 - 428 
7 - 302 
8 - 249 
9 - 688 
10 - 1387 
11 - 556424 
12 - 8192, best achieved
13 - 360841, personal best
14 - 2199
15 - 81
16 - 3968
17 - 1628
18 - 31652, personal best
19 - 18669, personal best
20 - 12134, personal best
21 - 12117, personal best
22 - 4521, personal best
23 - not solved
24 - not solved
25 - not solved
"""
