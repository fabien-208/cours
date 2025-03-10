
def DIJKSTRA(graphe :dict, depart) -> list[int]:

    dist = {noeud: float('inf') for noeud in graphe}
    dist[depart] = 0
    precedent = {noeud: None for noeud in graphe}
    non_visites = set(graphe.keys())
    
    while non_visites:
        u = min(non_visites, key=lambda noeud: dist[noeud])
        non_visites.remove(u)
        
        for v, poids in graphe[u].items():
            nouvelle_dist = dist[u] + poids
            if nouvelle_dist < dist[v]:
                dist[v] = nouvelle_dist
                precedent[v] = u
    
    return dist






graph = {
    'v1': {'v2': 14, 'v3': 9, 'v4':7},
    'v2': {'v1': 14, 'v5': 9},
    'v3': {'v1': 9, 'v4': 11, 'v6': 10},
    'v4': {'v1': 7, 'v3': 11, 'v6':15},
    'v5': {'v2': 9, 'v6': 6},
    'v6': {'v3': 10, 'v4':15, 'v5':6}
}

print(DIJKSTRA(graph, 'v1'))