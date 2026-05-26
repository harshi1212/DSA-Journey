"""
Minimum Spanning Tree
Kruskal's Algorithm using Union-Find
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskal_mst(n, edges):
    """
    Find MST using Kruskal's algorithm.
    
    Args:
        n: number of vertices
        edges: list of (weight, u, v)
    
    Returns:
        (total_weight, mst_edges)
    """
    # Sort edges by weight
    edges.sort()
    
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for weight, u, v in edges:
        # If u and v not connected, add edge
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
            # MST has n-1 edges
            if len(mst) == n - 1:
                break
    
    return total_weight, mst

def prim_mst(n, adj, start=0):
    """
    Find MST using Prim's algorithm.
    
    Args:
        n: number of vertices
        adj: adjacency list {u: [(v, weight), ...]}
        start: starting vertex
    
    Returns:
        (total_weight, mst_edges)
    """
    import heapq
    
    visited = [False] * n
    mst = []
    total_weight = 0
    
    # Min heap: (weight, u, v)
    heap = [(0, start, -1)]
    
    while heap:
        weight, u, parent = heapq.heappop(heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, weight))
            total_weight += weight
        
        # Add neighbors to heap
        for v, w in adj.get(u, []):
            if not visited[v]:
                heapq.heappush(heap, (w, v, u))
    
    return total_weight, mst

# Example 1: Kruskal's MST
print("=== Kruskal's MST ===\n")

n = 4
edges = [
    (1, 0, 1),  # (weight, u, v)
    (2, 0, 2),
    (3, 1, 2),
    (1, 1, 3),
    (2, 2, 3),
]

print("Edges (weight, u, v):")
for w, u, v in edges:
    print(f"  {u}-{v}: {w}")

total, mst = kruskal_mst(n, edges)
print(f"\nMST total weight: {total}")
print("MST edges:")
for u, v, w in mst:
    print(f"  {u}-{v}: {w}")

# Example 2: Prim's MST
print("\n=== Prim's MST ===\n")

adj = {
    0: [(1, 1), (2, 2)],
    1: [(0, 1), (2, 3), (3, 1)],
    2: [(0, 2), (1, 3), (3, 2)],
    3: [(1, 1), (2, 2)],
}

print("Graph adjacency list:")
for u in adj:
    print(f"  {u}: {adj[u]}")

total, mst = prim_mst(n, adj)
print(f"\nMST total weight: {total}")
print("MST edges:")
for u, v, w in mst:
    print(f"  {u}-{v}: {w}")

# Example 3: Real-world - network design
print("\n=== Real-World: Network Design ===\n")

cities = ['A', 'B', 'C', 'D', 'E']
n = len(cities)

# (cost, city1, city2)
connections = [
    (4, 0, 1),   # A-B: 4
    (2, 0, 3),   # A-D: 2
    (1, 1, 3),   # B-D: 1
    (5, 1, 2),   # B-C: 5
    (8, 2, 3),   # C-D: 8
    (10, 2, 4),  # C-E: 10
    (7, 3, 4),   # D-E: 7
]

print("Cities:", cities)
print("Connections (cost, city1, city2):")
for cost, u, v in connections:
    print(f"  {cities[u]}-{cities[v]}: ${cost}M")

total, mst = kruskal_mst(n, connections)

print(f"\nMinimum cost network: ${total}M")
print("Build connections:")
for u, v, cost in mst:
    print(f"  {cities[u]}-{cities[v]}: ${cost}M")

print("\n=== Complexity ===")
print("Kruskal:  O(E log E) - sorting dominates")
print("Prim:     O(E log V) - heap operations")
print("Both:     ~Same for dense graphs")
print("\nUse Kruskal if: edges easily available")
print("Use Prim if: adjacency list preferred")
