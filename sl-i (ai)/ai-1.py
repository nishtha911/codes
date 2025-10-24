from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}

def bfs(start, visited=None):
    if visited is None:
        visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(current, visited=None):
    if visited is None:
        visited = set()
    print(current, end=" ")
    visited.add(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(neighbor, visited)

print("BFS:")
bfs('A')

print("\nDFS:")
dfs('A')