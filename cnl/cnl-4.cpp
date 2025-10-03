#include <iostream>
#include <vector>
#include <limits>
using namespace std;

struct Edge {
    int u, v, w;
};

void bellmanFord(int V, int E, const vector<Edge>& edges, int src) {
    const int INF = numeric_limits<int>::max();
    vector<int> dist(V, INF);
    dist[src] = 0;

    for (int i = 1; i < V; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].u;
            int v = edges[j].v;
            int w = edges[j].w;
            if (dist[u] != INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    cout << "Distances from router " << src << ":\n";
    for (int i = 0; i < V; i++) {
        cout << "To " << i << " = ";
        if (dist[i] == INF) cout << "INF";
        else cout << dist[i];
        cout << "\n";
    }
}

int main() {
    int V, E;
    cout << "Enter number of routers and links: ";
    cin >> V >> E;

    vector<Edge> edges(E);
    cout << "Enter edges (u v cost):\n";
    for (int i = 0; i < E; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    int src;
    cout << "Enter source router: ";
    cin >> src;

    bellmanFord(V, E, edges, src);
    return 0;
}
