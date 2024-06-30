from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman1.txt"

"""
###.#...
...L..##
.#######
"""

G = LambdaMap(map_file)

"""
[[ 0  0  0 12  0 14  3  3]
 [15  7  7  7  7  5  0  0]
 [ 9  0  0  0  0  0  0  0]]
 
(1, 3)
"""

print(G.lazy_path) # UDLLLDURRRRRURRLLDLL

