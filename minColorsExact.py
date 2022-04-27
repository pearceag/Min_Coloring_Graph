# Lauren Dorval 
# Min Colored Graph Exact Code

import itertools as it

def checkNP(graph, colors):
    for x in graph:
        for y in graph[x]:
            if colors[x] == colors[y]:
                return False
    return True

def generatePossible(colors, graph, verts):
    clauses = list(it.product(colors, repeat=len(verts)))
    for x in range(len(clauses)):
        colors = {}
        for y in range(len(clauses[x])):
            colors[verts[y]] = clauses[x][y]
        is_NP = checkNP(graph, colors)
        if is_NP:
            return True
    return False 

def main():
    i = int(input())
    verticies = {}
    v = []
    for _ in range(i):
        temp = input().split()
        verticies[temp[0]] = temp[1:]
        v.append(temp[0])
    numColors = 0
    solved = False
    while not solved and numColors < len(verticies):
        numColors += 1
        colors = []
        for x in range(numColors):
            colors.append(x)
        solved = generatePossible(colors, verticies, v)
    print("Minimum number of colors:", numColors)
    

if __name__ == "__main__":
    main()