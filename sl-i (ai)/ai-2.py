def astar(graph, heuristic, start, goal):
    open_list = [start]
    closed_list = []
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        current = open_list[0]
        min_f = g_cost[current] + heuristic[current]
        for node in open_list:
            f = g_cost[node] + heuristic[node]
            if f < min_f:
                min_f = f
                current = node

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_list.remove(current)
        closed_list.append(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue
            new_g = g_cost[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif new_g >= g_cost.get(neighbor, 9999):
                continue

            g_cost[neighbor] = new_g
            parent[neighbor] = current

    return None


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 6)],
    'C': [('A', 3), ('B', 1), ('D', 2), ('E', 3)],
    'D': [('B', 6), ('C', 2), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}

print("Shortest Path:", astar(graph, heuristic, 'A', 'E'))
