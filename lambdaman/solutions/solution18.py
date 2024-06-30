from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman18.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman18 {G.lazy_path}")