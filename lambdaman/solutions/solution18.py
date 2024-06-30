from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman18.txt"

G = LambdaMap(map_file)

lazy_path = G.lazy_path()