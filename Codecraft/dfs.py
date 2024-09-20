def dfs_iterative(graph, start_vertex):
    stack = [start_vertex]
    visited = set()
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
if __name__ == "_main_":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }
    

    print("Iterative DFS traversal starting from vertex 0:")
    dfs_iterative(graph, 0)