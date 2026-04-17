# Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
# graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
# structure. 





# Undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

# -------- DFS (Recursive) --------
def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour, visited)

# -------- BFS (Without deque) --------
def bfs(start):
    visited = set()
    queue = [start]   # simple list as queue
    visited.add(start)
    
    front = 0   # acts like queue pointer
    
    while front < len(queue):
        node = queue[front]
        front += 1
        
        print(node, end=" ")
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# -------- Run both --------
print("DFS Traversal:")
dfs('A', set())

print("\nBFS Traversal:")
bfs('A')