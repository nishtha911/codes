graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 6},
    'C': {'A': 3, 'B': 1, 'D': 2, 'E': 3},
    'D': {'B': 6, 'C': 2, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

heuristic = {'A': 1, 'B': 1, 'C': 0, 'D': 1, 'E': 1}

def astar(start, goal):
    open_list = set([start])
    visited = set()

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: g_cost[x] + heuristic[x])

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_list.remove(current)
        visited.add(current)

        for node in graph[current]:
            if node in visited:
                continue

            cost = g_cost[current] + graph[current][node]

            if node not in open_list or cost < g_cost[node]:
                g_cost[node] = cost
                parent[node] = current
                open_list.add(node)

    return None

print("Shortest Path:", astar('A', 'C'))
