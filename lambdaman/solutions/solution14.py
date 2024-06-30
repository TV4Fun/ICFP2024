from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman14.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman14 {G.lazy_path}")
