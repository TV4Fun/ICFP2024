from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman6.txt"

"""
L.......................................................................................................................................................................................................
"""

G = LambdaMap(map_file)

lazy_path = G.lazy_path()