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

"""
[[ 5  3  7  7  7  6]
 [12  0  9 15 15 14]
 [13  6  0  9 15 14]
 [13 15  2  0  9 14]
 [13 10  0  4  0  8]
 [12  0  5 15  6  0]
 [ 9  3 11 11 11  2]]
(4, 3)
"""

print(G.lazy_path)  # DLRUDRDRLULUDDLLLUURURLDLDDRRRUUDDLLLUUUURLDDDDRRRUUDDLLLUUUUUURRDULLDDDDDDRRRUUDDLLLUUUUUURRRRDULLLLDDDDDDRRRUUDDLLLUUUUUURRRRRDDUULLLLLDDDDDDRRRUUDDLLLUUUUUURRRDDRDRDULULUULLLDDDDDDRRRUU

