# Lauren Dorval 
# Min Colored Graph Exact Code

import itertools as it

def checkNP(graph, colors):
    for x in graph:
        for y in graph[x]:
            # make sure none of the colors the vertex has an edge with is the same color
            if colors[x] == colors[y]:
                # if they are the same color there is no way this will be the case
                return False
    return True

def generatePossible(colors, graph, verts):
    # generate clauses 
    clauses = list(it.product(colors, repeat=len(verts)))
    for x in range(len(clauses)):
        colors = {}
        for y in range(len(clauses[x])):
            # save clause in dictionary with corresponding color
            colors[verts[y]] = clauses[x][y]
        # if it works we are done
        is_NP = checkNP(graph, colors)
        if is_NP:
            return True, colors
    return False, {}

def main():
    i = int(input())
    verticies = {}
    v = []
    # read in input
    for _ in range(i):
        temp = input().split()
        # add edges to verticies dictionary
        verticies[temp[0]] = temp[1:]
        # save each vertex in v array 
        v.append(temp[0])
    numColors = 0
    solved = False
    # look for num colors needed until it is found or every vertex is a different color
    while not solved and numColors < len(verticies):
        numColors += 1
        colors = []
        # create array of colors
        for x in range(numColors):
            colors.append(x)
        solved, colors = generatePossible(colors, verticies, v)
    for color in colors:
        print("Vertex " + str(color), "---> Color " + str(colors[color]))
    print("Minimum number of colors:", numColors)
    

if __name__ == "__main__":
    main()