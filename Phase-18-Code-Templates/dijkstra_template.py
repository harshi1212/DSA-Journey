"""
TEMPLATE: Dijkstra's Algorithm
Use for: Shortest path from one source
Complexity: O((V + E) log V) with min-heap
"""

import heapq
from collections import defaultdict

def dijkstra(n, adj, start):
    """
    Shortest path from start to all vertices.
    
    Args:
        n: number of vertices
        adj: adjacency list {u: [(v, weight), ...]}
        start: source vertex
    
    Returns:
        distances, previous nodes
    """
    dist = [float('inf')] * n
    dist[start] = 0
    prev = [-1] * n
    
    heap = [(0, start)]  # (distance, vertex)
    visited = [False] * n
    
    while heap:
        d, u = heapq.heappop(heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        if d > dist[u]:
            continue
        
        for v, w in adj.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    
    return dist, prev

def reconstruct_path(prev, start, end):
    """Reconstruct path from start to end"""
    path = []
    current = end
    
    while current != -1:
        path.append(current)
        current = prev[current]
    
    path.reverse()
    return path if path[0] == start else []

# Usage:
print("Template 4: Dijkstra")

adj = {
    0: [(1, 4), (2, 2)],
    1: [(3, 1)],
    2: [(1, 1), (3, 5)],
    3: [],
}

dist, prev = dijkstra(4, adj, 0)
print(f"Distances from 0: {dist}")
print(f"Path 0→3: {reconstruct_path(prev, 0, 3)}")
