#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int n, e, src;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> e;

    vector<vector<int>> edges;
    cout << "Enter edges (u v w):\n";
    for(int i=0;i<e;i++){
        int u,v,w;
        cin >> u >> v >> w;
        edges.push_back({u,v,w});
    }

    cout << "Enter source node: ";
    cin >> src;

    vector<int> dist(n, INT_MAX);
    dist[src] = 0;

    for(int i=0;i<n-1;i++){
        for(auto &edge : edges){
            int u=edge[0], v=edge[1], w=edge[2];
            if(dist[u]!=INT_MAX && dist[u]+w < dist[v])
                dist[v] = dist[u]+w;
        }
    }

    cout << "\nDistance Vector Routing Result:\n";
    for(int i=0;i<n;i++)
        cout << "Node " << src << " -> " << i << " = " << dist[i] << endl;

    return 0;
}
