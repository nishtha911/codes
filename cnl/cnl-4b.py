def distance_vector_routing(graph):
    nodes = list(graph.keys())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}


    for u in nodes:
        dist[u][u] = 0
        for v, w in graph[u].items():
            dist[u][v] = w

    changed = True
    while changed:
        changed = False
        for u in nodes:
            for v in nodes:
                for n in graph[u]:  
                    if dist[u][v] > graph[u][n] + dist[n][v]:
                        dist[u][v] = graph[u][n] + dist[n][v]
                        changed = True
    return dist


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

result = distance_vector_routing(graph)

print("\n--- Distance Vector Routing ---")
for node in result:
    print(f"Node {node}: {result[node]}")
