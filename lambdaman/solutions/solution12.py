from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman12.txt"

G = LambdaMap(map_file)

print(G.lazy_path)