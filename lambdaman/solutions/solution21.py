from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman21.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman21 {G.lazy_path}")