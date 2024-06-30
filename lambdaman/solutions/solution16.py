from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman16.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman16 {G.lazy_path}")