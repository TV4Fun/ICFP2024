from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman15.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman15 {G.lazy_path}")