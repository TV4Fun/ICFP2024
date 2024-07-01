from typing import List, Tuple, NamedTuple
from collections import Counter

CONTROLS = {
    7: (-1, 1),
    8: (0, 1),
    9: (1, 1),
    5: (0, 0),
    4: (-1, 0),
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


def parse_input(input_str: str) -> Counter:
    coordinates = Counter()
    for line in input_str.strip().split("\n"):
        try:
            x, y = map(int, line.split())
            coordinates[(x, y)] += 1
        except ValueError as e:
            print(f"Error parsing line: {line}")
            print(f"Error message: {str(e)}")
            continue

    if not coordinates:
        raise ValueError("No valid coordinates found in the input")

    return coordinates


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def find_best_move(state: State, coordinates: Counter) -> Tuple[int, Tuple[int, int]]:
    best_command = None
    best_coord = None
    min_distance = float("inf")
    min_velocity_sum = float("inf")

    for coord, count in coordinates.items():
        if count > 0:
            for command, (dvx, dvy) in CONTROLS.items():
                new_x = state.x + state.vx + dvx
                new_y = state.y + state.vy + dvy
                new_vx = state.vx + dvx
                new_vy = state.vy + dvy
                distance = manhattan_distance(new_x, new_y, coord[0], coord[1])
                velocity_sum = abs(new_vx) + abs(new_vy)

                if distance < min_distance or (
                    distance == min_distance and velocity_sum < min_velocity_sum
                ):
                    min_distance = distance
                    min_velocity_sum = velocity_sum
                    best_command = command
                    best_coord = coord

    return best_command, best_coord


def navigate(coordinates: Counter) -> str:
    state = State(0, 0, 0, 0)
    nav_plan = []

    while coordinates:
        best_command, best_coord = find_best_move(state, coordinates)

        if best_command is None:
            # No direct keystroke to any remaining coordinate, try to get closer
            best_distance = float("inf")
            for command, (dvx, dvy) in CONTROLS.items():
                new_x = state.x + state.vx + dvx
                new_y = state.y + state.vy + dvy
                distance = min(
                    manhattan_distance(new_x, new_y, coord[0], coord[1])
                    for coord in coordinates
                )
                if distance < best_distance:
                    best_distance = distance
                    best_command = command

        if best_command is None:
            break

        nav_plan.append(str(best_command))

        new_x = state.x + state.vx + CONTROLS[best_command][0]
        new_y = state.y + state.vy + CONTROLS[best_command][1]

        # Check if we've hit a coordinate
        if (new_x, new_y) in coordinates:
            coordinates[(new_x, new_y)] -= 1
            if coordinates[(new_x, new_y)] == 0:
                del coordinates[(new_x, new_y)]

        state = State(
            new_x,
            new_y,
            state.vx + CONTROLS[best_command][0],
            state.vy + CONTROLS[best_command][1],
        )

    return "".join(nav_plan)


# # Example usage
# input_str = """
# -124 -159
# -35 -92
# -168 -175
# -198 -173
# -199 -171
# -45 -102
# -158 -167
# -195 -174
# -4 -25
# -190 -177
# -184 -167
# -75 -130
# -141 -168
# -102 -145
# -175 -172
# -15 -60
# -1 -5
# -149 -168
# -188 -169
# -181 -167
# -199 -169
# -151 -167
# -78 -138
# -173 -173
# -181 -179
# -156 -166
# -73 -127
# -76 -134
# -7 -34
# -172 -177
# -64 -119
# -30 -89
# -85 -143
# -13 -54
# -18 -73
# -198 -168
# 0 -3
# -115 -151
# -52 -109
# -170 -172
# -172 -172
# -197 -174
# -167 -172
# -188 -178
# 0 -1
# -186 -168
# -179 -168
# -71 -124
# -2 -10
# -165 -173
# -42 -99
# -160 -168
# -3 -21
# -173 -174
# -178 -169
# -177 -178
# -144 -168
# -81 -141
# -10 -49
# -185 -179
# -94 -144
# -197 -168
# -193 -169
# -56 -112
# -39 -96
# -133 -165
# -194 -174
# -68 -122
# -1 -7
# -195 -168
# -23 -82
# -8 -43
# -111 -148
# -163 -170
# -194 -175
# -173 -174
# -106 -146
# -120 -155
# -98 -145
# -175 -173
# -21 -78
# -60 -116
# -146 -168
# -193 -176
# -174 -174
# -2 -13
# -7 -38
# -137 -167
# -176 -170
# -193 -175
# -191 -169
# -192 -176
# -16 -67
# -48 -106
# -6 -29
# -3 -17
# -128 -162
# -26 -86
# -90 -144
# -154 -166
# """

# coordinates = parse_input(input_str)
# nav_plan = navigate(coordinates)
# print("Navigation plan:", nav_plan)
# print(len(nav_plan))
