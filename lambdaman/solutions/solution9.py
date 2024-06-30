from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman9.txt"

"""
L.................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
"""

G = LambdaMap(map_file)

"""
[[ 5  7  7 ...  7  7  6]
 [13 15 15 ... 15 15 14]
 [13 15 15 ... 15 15 14]
 ...
 [13 15 15 ... 15 15 14]
 [13 15 15 ... 15 15 14]
 [ 9 11 11 ... 11 11 10]]
(0, 0)
"""

print(G.lazy_path) # RDULRRRDULLLRRRRRDULLLLLRRRRRRRDULLLLLLLRRRRRRRRRDULLLLLLLLLRRRRRRRRRRRDULLLLLLLLLLLRRRRRRRRRRRRRDULLLLLLLLLLLLLRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRLULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRLULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRLULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRLULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLLLDDDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUUUURRRRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLLLDDDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUUUURRRRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLLLDDDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUUUURRRRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLLLDDDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUUUURRRRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLLLDDDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUUUURRRRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLLLDDDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUUUURRRRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULLLLDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRLULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUURRDDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUULL