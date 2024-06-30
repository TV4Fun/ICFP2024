from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman21.txt"

G = LambdaMap(map_file)

lazy_path = G.lazy_path()