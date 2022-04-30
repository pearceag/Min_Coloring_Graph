"""
    name: Brooke Sindelar

"""
import random
from xmlrpc.client import MAXINT
import min_colors_exact, min_colors_approx
import time

# function to run several variable-sized graph tests
def main():
    # initialization of graph data structures
    connections = {}
    vertex_list = []

    # these values can be easily changed
    # upper bound of vertex count
    max_vertices = 30
    # initial upper bound of edge count for an undirected graph
    max_edges = 29

    num_edges = 0
    num_vertices = 0

    # generate a random number of vertices bounded by the max
    num_vertices = int((random.random() * MAXINT) % max_vertices)
    # set max edge count to be the vertex count - 1
    if num_vertices > 1:
        max_edges = num_vertices - 1
        # generate a random number of edges bounded by the max
        num_edges = int((random.random() * MAXINT) % max_edges)

    # set initial values for graph data structures
    for vertex in range(num_vertices):
        connections[vertex] = []
        vertex_list.append(vertex)

    # loop over the number of edges
    for _ in range(num_edges):
        # choose two random nodes from the graph to be connected
        node1 = int((random.random() * MAXINT) % num_vertices)
        node2 = int((random.random() * MAXINT) % num_vertices)            

        # add them both to each others connection list bc undirected
        if node1 != node2:
            connections[node1].append(node2)
            connections[node2].append(node1)

    # keeping this in for easy error checking
    print("connections:", connections)

    # create file for graph construction retention
    graph_file = open("random_test_output.txt", "w")

    # write first line of input
    graph_file.write(str(num_vertices) + "\n")
    temp_str = ""

    # loop over the number of vertices
    for i in range(num_vertices):
        # if the current vertex is connected to anything else
        if len(connections[i]) > 0:
            # make a string of its connected nodes
            for j in connections[i]:
                temp_str = str(j) + " "
        # otherwise it should be an empty string
        else:
            temp_str = ""
        # format remaining input lines
        connected_nodes = str(i) + " " + temp_str + "\n"
        # write that to the file
        graph_file.write(connected_nodes)
    graph_file.close()

    # start timing approximation solution
    approx_start = time.time()
    # run approximation
    min_colors_approx.find_approx_min_coloring(connections, num_vertices)
    approx_end = time.time()
    # print out the timings
    print("approx solution wall clock time:", approx_end - approx_start)

    # start running exact solution
    numColors = 0
    solved = False
    # start timing
    exact_start = time.time()
    while not solved and numColors < len(connections):
        numColors += 1
        colors = []
        # create array of colors
        for x in range(numColors):
            colors.append(x)
        # call the exact solution function
        solved, colors = min_colors_exact.generatePossible(colors, connections, vertex_list)
        for color in colors:
            print("Vertex " + str(color), "---> Color " + str(colors[color]))
        print("Minimum number of colors:", numColors)
    # end timing
    exact_end = time.time()
    # print out exact solution time
    print("exact solution wall clock time:", exact_end - exact_start)

# utility to run main function
if __name__ == "__main__":
    main()