from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman19.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman19 {G.lazy_path}")