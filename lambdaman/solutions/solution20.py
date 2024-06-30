from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman20.txt"

G = LambdaMap(map_file)

print(f"solve lambdaman20 {G.lazy_path}")