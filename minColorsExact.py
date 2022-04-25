# Lauren Dorval 
# Min Colored Graph Exact Code

import itertools as it

def checkNP(colors, graph, verts):
    pass

def generatePossible(colors, graph, verts):
    clauses = list(it.product(colors, repeat=len(graph)))
    is_NP = False
    for x in range(len(clauses)):
        is_NP = checkNP(graph, clauses[x], verts)
        if is_NP:
            break

def main():
    i = int(input())
    verticies = {}
    v = []
    for _ in range(i):
        temp = input().split()
        verticies[temp[0]] = temp[1:]
        v.append(temp[0])
    numColors = 1
    solved = False
    while not solved and numColors < len(verticies):
        colors = []
        for x in range(numColors):
            colors.append(x)
        solved = generatePossible(colors, verticies, v)
        numColors += 1

if __name__ == "__main__":
    main()