import sys

def find_approx_min_coloring(graph, v):

    result = [-1] * v
    
    # Assign the first color to first vertex
    start = graph[0]
    # max = -sys.maxsize
    # for key in graph:
    #     if len(graph[key]) > max:
    #         max = len(graph[key])
    #         start = key
    result[start] = 0
    min_colors = 1
 
 
    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * v
 
    # Assign colors to remaining V-1 vertices
    for u in range(1, v):
         
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in graph[u]:
            if (result[int(i)] != -1):
                min_colors += 1
                available[result[int(i)]] = True

 
        # Find the first available color
        cr = 0
        while cr < v:
            if (available[cr] == False):
                break
             
            cr += 1
             
        # Assign the found color
        result[u] = cr
 
        # Reset the values back to false
        # for the next iteration
        for i in graph[u]:
            if (result[int(i)] != -1):
                available[result[int(i)]] = False
 
    # Print the result
    print(min_colors)

def main():
    i = int(input())
    graph = {}
    v = []
    for _ in range(i):
        temp = input().split()
        graph[int(temp[0])] = temp[1:]
        v.append(temp[0])
  
    find_approx_min_coloring(graph, len(v))

if __name__ == "__main__":
    main()