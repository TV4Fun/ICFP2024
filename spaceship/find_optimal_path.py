import math
from typing import List, Tuple

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


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def navigate(coordinates: List[Tuple[int, int]]) -> List[int]:
    path = []
    position = [0, 0]
    velocity = [0, 0]

    for target in coordinates:
        while position[0] != target[0] or position[1] != target[1]:
            best_control = 5  # Default to no change
            min_distance = float("inf")

            for control, dv in CONTROLS.items():
                new_velocity = [velocity[0] + dv[0], velocity[1] + dv[1]]
                new_position = [
                    position[0] + new_velocity[0],
                    position[1] + new_velocity[1],
                ]
                dist = distance((new_position[0], new_position[1]), target)

                if dist < min_distance:
                    min_distance = dist
                    best_control = control

            path.append(best_control)
            dv = CONTROLS[best_control]
            velocity[0] += dv[0]
            velocity[1] += dv[1]
            position[0] += velocity[0]
            position[1] += velocity[1]

    return path


def parse_input(input_str: str) -> List[Tuple[int, int]]:
    coordinates = []
    for line in input_str.strip().split("\n"):
        x, y = map(int, line.split())
        coordinates.append((x, y))
    return coordinates


def main():
    # replace input_str string with coordinate list
    input_str = """"""

    coordinates = parse_input(input_str)

    path = navigate(coordinates)

    print("Navigation path:")
    print("".join(map(str, path)))
    print(f"Total number of moves: {len(path)}")


if __name__ == "__main__":
    main()
