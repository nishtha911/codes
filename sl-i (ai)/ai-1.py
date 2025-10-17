from collections import deque

g = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}

def bfs(s, v=None):
    if v is None:
        v = set()
    q = deque([s])
    v.add(s)
    while q:
        n = q.popleft()
        print(n, end=" ")
        for nei in g[n]:
            if nei not in v:
                v.add(nei)
                q.append(nei)

def dfs(n, v=None):
    if v is None:
        v = set()
    print(n, end=" ")
    v.add(n)
    for nei in g[n]:
        if nei not in v:
            dfs(nei, v)

print("BFS:")
bfs('A')

print("\nDFS:")
dfs('A')
