import math
import numpy as np
import random
from itertools import permutations

# FUNCTIONS ####################################################

# Check to make sure the adjacency table is symmetric across the main diagonal.
# This is a required property for the table to be a valid adjacency table.
# For example, if A-B has weight 2, B-A must also have weight 2.

def is_commutative(table):
    com = ''
    for i in range(0, n):
        for j in range(0, n):
            if table[i][j] == table[j][i]:
                com = com + 'Y'

    if len(com) == n**2:
        return True
    else:
        return False

def connected(table, x, y):
    if table[x - 1][y - 1] != 0:
        return True
    else:
        return False

# This function calculates the number of non-zero numbers in one row of the table.
# This represents the order of a vertex, or the number of edges coming out of it.
def order(table, vertex_num):
    order = 0
    for i in range(0, n):
        if table[vertex_num - 1][i] != 0:
            order += 1

    return order


# This function calculate the size of the graph (the number of edges it contains).
# The value of the variable "size" is incremented by 1 only if the entry in the table is non-zero.
# This is because an entry of zero would mean that the vertices are not connected.
def graph_size(table):
    size = 0
    for i in range(0, n):
        for j in range(i, n):
            if table[i][j] != 0:
                size += 1

    return size


# Check to make sure the path is valid.
# Consecutive vertices must be connected in order for the function to return True.
# For example: if [1, 2, 3, 4] is the path, vertex 1 must be connected to 2, 2 to 3, and 3 to 4.

# The function sets up pairs of consecutive vertices to make the analysis easier.
# The pairs generated in the above example would be [1, 2], [2, 3], and [3, 4].
# The function will now check whether the vertices within each of those three pairs are connected.
# If a vertex pair passes the test, it will be added to a new list called "connections."

# In a valid path, all vertex pairs would be added to "connections".
# Thus in order for the function to return True, the list "pairs" must equal the list "connections."

def valid_path(table, path):
    pairs = []
    for i in range(len(path)-1):    
        pairs.append([path[i], path[i+1]])

    connections = []
    for i in range(len(path)-1):    
        if connected(table, path[i], path[i + 1]) == True:
            connections.append([path[i], path[i+1]])

    if connections == pairs:
        return True
    else:
        return False

# This function forms the crux of the program.

# The function first creates a list of all vertices in the graph (all_vertices).
# For example, if the graph has 6 vertices, all_vertices = [1, 2, 3, 4, 5, 6].
# The start and end vertices are then removed, because we need to find all possible arrangements (permutations) of only [2, 3, 4, 5].
# We know that 1 and 6 must be included as those are the start and end vertices.

# The function then finds all possible arrangements of [2, 3, 4, 5] and adds each arrangement to a list called "perms."
# For example:
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 5, 4, 6]
# [1, 3, 2, 4, 5, 6]
# [1, 3, 2, 5, 4, 6]
# ...

# However, we don't need to use each vertex in the minimum connector problem.
# As a result, we must also find arrangements of a smaller length, which don't use all vertices.
# For example, permutations of length 5 would not use 1 vertex:
# [1, 2, 3, 4, 6] (does not use vertex 5)
# [1, 2, 3, 5, 6] (does not use vertex 4)
# [1, 3, 4, 2, 6] (does not use vertex 5)
# [1, 3, 4, 5, 6] (does not use vertex 2)
# ...

# Permutations of length 4 would now be found:
# [1, 2, 3, 6]
# [1, 2, 4, 6]
# [1, 2, 5, 6]
# [1, 3, 4, 6]
# ...

# This process continues until the permutation length is reduced to its minimum.

# Now that all permutations are printed, the function checks every generated permutation for path validity using the "valid_path" function.
# This is because not all permutations may actually be paths!
# For example, in the permutation [1, 3, 4, 6] shown above, if 3 and 4 are not connected, the path is not valid!

# All permutations that pass the path validity test are added to a list called "allpaths."

def all_possible_paths(table, start, end):
    all_vertices = list(range(1, len(table)+1))
    all_vertices.remove(start)
    all_vertices.remove(end)
    
    entire_list = []
    for r in range(0, n - 2):
        chooseV = all_vertices
        perms = []
        for i in list(permutations(chooseV, len(chooseV) - r)):
            i = list(i)
            i.insert(0, start)
            i.insert(len(i), end)
            perms.append(i)
        entire_list.append(perms)

    numpaths = 0
    allpaths = []
    for path_group in entire_list:
        for path in path_group:
            if valid_path(table, path) == True:
                allpaths.append(path)
                numpaths += 1

    return allpaths

# This function calculates the total weight of a given path by adding together the weights of all edges in the path.
# For example, the total weight of path [1, 2, 3, 4] is the sum of:
# - The weight of edge 1-2
# - The weight of edge 2-3
# - The weight of edge 3-4

# Just like the "valid_path" function, this function creates pairs of vertices to make analysis easier and compute the weights of an edge one at a time.

def path_weight(table, path):
    pairs = []

    for i in range(0, len(path) - 1):
        pairs.append([path[i], path[i + 1]])

    weight = 0
    for pair in pairs:
        weight += table[pair[0]-1][pair[1]-1]

    return weight


# This function outputs the ultimate result.
# It considers all paths between the start and end vertices, and calculates the weight of each of those paths.

# The program first calculates the smallest value in the list "allweights", retrieves that value's index, and outputs the path corresponding to that index.
# This is the minimum weight path!

def minimum_path(table, start, end):
    allpaths = all_possible_paths(table, start, end)

    allweights = []
    
    for path in allpaths:
        allweights.append(path_weight(table, path))

    min_weight = min(allweights)
    
    i = allweights.index(min_weight)
    return [allpaths[i], min_weight]

# This function sorts all of the paths generated by all_possible_paths() in order of increasing weight.
def sort_all_paths(table, start, end):
    allpaths = all_possible_paths(table, start, end)
    allweights = []
    for path in allpaths:
        allweights.append(path_weight(table, path))

    path_dictionary = []
    for path in allpaths:
        path_dictionary.append([path_weight(table, path), path])

    path_dictionary.sort()
    return path_dictionary

################################################################

while True:
    n = int(input('How many vertices does your graph have? '))
    print('')
    table = []
    for i in range(n):
        table.append([0] * n)

    for i in range(0, n):
        for j in range(i+1, n):
            table[i][j] = float(input('Enter the weight of the edge connecting vertices ' + str(i + 1) + ' and ' + str(j+1) + ': '))
            table[j][i] = table[i][j]
            table[i][i] = 0
            
    print('')

    # This is the adjacency table representing the graph.
    # The first step in the program would be to display the table in a much neater form: an array (using numpy).
    
    print(np.array(table))
    print('')

    if is_commutative(table) == False:
        print('ERROR: The adjacency table is not commutative.')
        
    else:
        start = int(input('What is the starting vertex? '))
        end = int(input('What is the ending vertex? '))
        print('')
        
        allpaths = sort_all_paths(table, start, end)
        minpath = minimum_path(table, start, end)

        print(str(len(allpaths)) + ' possible paths from vertex ' + str(start) + ' to vertex ' + str(end) + ':')
        for path in allpaths:
            if path[0] != minpath[1]:
                string = ''
            else:
                string = 'MINIMUM WEIGHT PATH: '

            print(string + str(path[1]) + ' with weight ' + str(path[0]) + '.')
    
    print('*********************************************************************')
    print('')
