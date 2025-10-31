import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessors = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def get_path(predecessors, target_node):
    path = []
    current_node = target_node
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    return path[::-1]

graph_ls = {
    'A': {'B': 10, 'C': 3},
    'B': {'A': 10, 'D': 2, 'E': 4},
    'C': {'A': 3, 'D': 8, 'F': 2},
    'D': {'B': 2, 'C': 8, 'E': 5, 'F': 20},
    'E': {'B': 4, 'D': 5, 'G': 15},
    'F': {'C': 2, 'D': 20, 'G': 5},
    'G': {'E': 15, 'F': 5}
}

source = 'A'
shortest_distances, paths = dijkstra(graph_ls, source)

print("Link State (Dijkstra's) Results")
print("Shortest distances from node", source + ":")
print(shortest_distances)

target = 'G'
shortest_path = get_path(paths, target)
print("Shortest path from", source, "to", target + ":", shortest_path)