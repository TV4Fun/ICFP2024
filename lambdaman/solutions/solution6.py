from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman6.txt"

"""
L.......................................................................................................................................................................................................
"""

G = LambdaMap(map_file)

lazy_tsp = G.lazy_tsp()


# this is not the method used to solve
print(f"solve lambdaman6 {lazy_tsp}")

# B$ L! B$ v! B$ v! B$ v! SLLLL L! B. B. v! v! B. v! v!