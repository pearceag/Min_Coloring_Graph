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
    num_vertices = 20
    num_edges = 30

    # set initial values for graph data structures
    for vertex in range(num_vertices):
        connections[vertex] = []
        vertex_list.append(vertex)

    i = 0
    # loop over the number of edges
    while i < num_edges:
        # choose two random nodes from the graph to be connected
        node1 = int((random.random() * MAXINT) % num_vertices)
        node2 = int((random.random() * MAXINT) % num_vertices)            

        # add them both to each others connection list bc undirected
        if node1 != node2 and node2 not in connections[node1] and node1 not in connections[node2]:
            connections[node1].append(node2)
            connections[node2].append(node1)
            i += 1

    print("connections:", connections)

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