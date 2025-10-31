def distance_vector_routing(graph):
    nodes = list(graph.keys())
    distance_vectors = {node: {n: float('inf') for n in nodes} for node in nodes}
    for node in nodes:
        distance_vectors[node][node] = 0
    
    for u in nodes:
        for v, weight in graph[u].items():
            distance_vectors[u][v] = weight

    while True:
        updated = False
        new_distance_vectors = {u: dv.copy() for u, dv in distance_vectors.items()}
        
        for u in nodes: 
            for v in nodes: 

                min_dist = distance_vectors[u][v]
                for w in graph[u]: 
                   
                    path_cost = graph[u][w] + distance_vectors[w][v]
                    
                    if path_cost < min_dist:
                        min_dist = path_cost
                        updated = True
                
                new_distance_vectors[u][v] = min_dist

        distance_vectors = new_distance_vectors
        
        if not updated:
            break

    return distance_vectors

graph_dv = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

final_distance_vectors = distance_vector_routing(graph_dv)

print("\nDistance Vector Routing Results")
print("Final Routing Tables (Shortest Distances to all destinations):")
for node, dv in final_distance_vectors.items():
    print("Node", node + ":", dv)