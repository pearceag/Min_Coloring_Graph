import sys
'''
Author: Lexie Pearce

Citations: 
    https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/ 
    https://en.wikipedia.org/wiki/Greedy_coloring 
    https://en.wikipedia.org/wiki/Graph_coloring#Polynomial_time
'''

def find_approx_min_coloring(graph, v):
    result = [-1] * v
    
    # Assign the first color to first vertex    
    result[0] = 0
 
    # A temporary array to store the available colors.
    # True value of available_colors[color] would mean that the
    # color is assigned to one of its adjacent vertices
    available_colors = [False] * v
 
    # Assign colors to remaining vertices
    for u in range(0, v):
         
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in graph[u]:
            if (result[i] != -1):
                available_colors[result[i]] = True
    
        # Find the first available color
        color = 0
        while color < v:
            if (available_colors[color] == False):
                break
            color += 1
             
        # Assign the found color
        result[u] = color
 
        # Reset the values back to false
        # for the next iteration
        for i in graph[u]:
            if (result[i] != -1):
                available_colors[result[i]] = False
    
    # Print the result
    for u in range(v):
        print("Vertex", u, " --->  Color", result[u])
    print("Minimum number of colors:", color + 1) # Minimum colors would be equal to the last color assignment + 1

def main():
    i = int(input())
    graph = [[] for i in range(i)]
    v = []
    for _ in range(i):
        temp = input().split()
        for i in temp[1:]:
            if int(i) not in graph[int(temp[0])]:
                graph[int(temp[0])].append(int(i))
            if int(temp[0]) not in graph[int(i)]:
                graph[int(i)].append(int(temp[0]))
        v.append(temp[0])
    find_approx_min_coloring(graph, len(v))

if __name__ == "__main__":
    main()