from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman15.txt"

G = LambdaMap(map_file)

lazy_path = G.lazy_path()