# Graph Theory: Background
In discrete mathematics, a graph is a structure that consists of multiple vertices connected to other vertices by edges. Each edge is assigned a particular number – called a weight – which could represent distance, cost, travel time, etc. between two vertices. A graph is mathematically represented by an adjacency matrix (also called an adjacency table). This is a n × n square matrix (where n is the number of vertices in the graph) containing information about which vertices in the graph are connected to other vertices.

Note that adjacency matrices are generally symmetric about the main diagonal, i.e. if vertex A is connected to vertex B, then vertex B must also be connected to vertex A. If this symmetry exists, the graph is referred to as undirected.

Graph theory is simply the study of such graphs and their properties. The minimum connector problem is a common problem in graph theory – it aims to find the path of least weight between two given vertices. This problem is very applicable in the real world – for example, vertices in a graph can represent cities, and edges can represent roads between those cities. In this case, the minimum connector problem can be implemented to determine the shortest/fastest path between two particular cities.

# The Project
Dijkstra’s algorithm is typically used to solve the minimum connector problem; however, a trial and error approach can also be used, provided that the number of vertices and edges on the graph is relatively small. In mathematics, this approach is called inspection, and its computational equivalent is the brute-force method.

The program first asks the user to input the number of vertices in the graph, and then to enter the weights connecting each vertex. For example, it will ask for the weight of the edge connecting vertices 1 and 2, 1 and 3, …, 1 and n. Then it will ask for the weight of the edge connecting vertices 2 and 3, 2 and 4, …, 2 and n, and so on. Note that the program only works for simple graphs. In a simple graph, two vertices are connected by no more than one edge, and there are no loops (a vertex connected to itself). Graphs that do not satisfy these properties are referred to as multigraphs.

Using the weights, the program executes the all_possible_paths() function (user-defined), which calculates all permutations (all possible arrangements) of the vertex numbers (except for the start and end vertex, because those must stay fixed). However, the minimum-weight path in a graph does not need to hit every vertex, and so smaller permutations must be considered as well. But it is important to note that these permutations are merely arrangements of the vertex numbers, they do not necessarily represent valid paths. As a result, the valid_path() function checks to make sure that the vertices in each of these permutations are actually connected.

Finally, the program runs the minimum_path() function, which analyzes the output of the all_possible_paths() function. It then finds the minimum weight of all of these paths, and outputs the path corresponding to this minimum weight. The program’s ultimate output is the minimum-weight path, along with alternative (yet longer) paths one can traverse to get from the starting vertex to the ending vertex.

I definitely consider this project to be the most challenging I have done so far, as it involves a highly sophisticated, complex combination of for loops and if-else conditional statements. However, I feel proud to have completed this project, as it allowed me to solidify my Python skills, and it investigates a pure mathematics problem that has real-life applications!
