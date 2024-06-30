from lambdaman.lambdagraph import LambdaMap

map_file = "..//problems/lambdaman8.txt"

"""
###################################################################################################
#.................................................................................................#
#.###############################################################################################.#
#.#.............................................................................................#.#
#.#.###########################################################################################.#.#
#.#.#.........................................................................................#.#.#
#.#.#.#######################################################################################.#.#.#
#.#.#.#.....................................................................................#.#.#.#
#.#.#.#.###################################################################################.#.#.#.#
#.#.#.#.#.................................................................................#.#.#.#.#
#.#.#.#.#.###############################################################################.#.#.#.#.#
#.#.#.#.#.#.............................................................................#.#.#.#.#.#
#.#.#.#.#.#.###########################################################################.#.#.#.#.#.#
#.#.#.#.#.#.#.........................................................................#.#.#.#.#.#.#
#.#.#.#.#.#.#.#######################################################################.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.....................................................................#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.###################################################################.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.................................................................#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.###############################################################.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.............................................................#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.###########################################################.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.........................................................#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#######################################################.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.....................................................#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.###################################################.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.................................................#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.###############################################.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.............................................#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.###########################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.........................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#######################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.....................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###############################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.............................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###########################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.........................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#######################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.....................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###############.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.............#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#######.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.....#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#L#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#####.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...........#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#############.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...............#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#####################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#########################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...........................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#############################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...............................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#...................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#####################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.......................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#.#########################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#...........................................#.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#.#############################################.#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#...............................................#.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#.#################################################.#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#...................................................#.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.#####################################################.#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#.......................................................#.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#.#########################################################.#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#...........................................................#.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#.#############################################################.#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#...............................................................#.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#.#################################################################.#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#...................................................................#.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#####################################################################.#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.......................................................................#.#.#.#.#.#.#.#
#.#.#.#.#.#.#########################################################################.#.#.#.#.#.#.#
#.#.#.#.#.#...........................................................................#.#.#.#.#.#.#
#.#.#.#.#.#############################################################################.#.#.#.#.#.#
#.#.#.#.#...............................................................................#.#.#.#.#.#
#.#.#.#.#################################################################################.#.#.#.#.#
#.#.#.#...................................................................................#.#.#.#.#
#.#.#.#####################################################################################.#.#.#.#
#.#.#.......................................................................................#.#.#.#
#.#.#########################################################################################.#.#.#
#.#...........................................................................................#.#.#
#.#############################################################################################.#.#
#...............................................................................................#.#
#################################################################################################.#
..................................................................................................#
###################################################################################################
"""

G = LambdaMap(map_file)

print(G.map)
print(G.origin)

"""
[[ 0  0  0 ...  0  0  0]
 [ 0  5  3 ...  3  6  0]
 [ 0 12  0 ...  0 12  0]
 ...
 [ 0  0  0 ...  0 12  0]
 [ 1  3  3 ...  3 10  0]
 [ 0  0  0 ...  0  0  0]]
(49, 49)
"""

print(G.lazy_path) # DDLLUUUURRRRDDDDDDLLLLLLUUUUUUUURRRRRRRRDDDDDDDDDDLLLLLLLLLLUUUUUUUUUUUURRRRRRRRRRRRDDDDDDDDDDDDDDLLLLLLLLLLLLLLUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL