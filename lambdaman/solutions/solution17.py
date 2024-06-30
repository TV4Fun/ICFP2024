from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman17.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman17 {G.lazy_path}")