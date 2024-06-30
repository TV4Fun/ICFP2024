from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman13.txt"

G = LambdaMap(map_file)

print(G.lazy_path)