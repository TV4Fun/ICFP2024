from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman2.txt"

"""
L...#.
#.#.#.
##....
...###
.##..#
....##
"""

G = LambdaMap(map_file)

"""
[[ 1  7  3  6  0  4]
 [ 0  8  0 12  0 12]
 [ 0  0  5 11  3 10]
 [ 5  3 10  0  0  0]
 [12  0  0  5  2  0]
 [ 9  3  3 10  0  0]]

(0, 0)
"""

print(G.lazy_path)  # RDULRRRDDRRUUDDLLUULLLRRRDDLDLLDDRRRURLDLLLUURRURUULLL

