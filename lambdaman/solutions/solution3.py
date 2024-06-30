from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman3.txt"

"""
......
.#....
..#...
...#..
..#L#.
.#...#
......
"""

G = LambdaMap(map_file)

lazy_path = G.lazy_path()
