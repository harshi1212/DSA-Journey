"""
TEMPLATE: Graph Traversal (BFS/DFS)
Use for: Connected components, reachability, topological sort
Complexity: O(V + E)
"""

from collections import deque

def bfs_traversal(n, adj, start=0):
    """BFS from start vertex"""
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in adj.get(u, []):
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    return result

def dfs_traversal(n, adj, start=0):
    """DFS from start vertex"""
    visited = [False] * n
    result = []
    
    def dfs(u):
        visited[u] = True
        result.append(u)
        
        for v in adj.get(u, []):
            if not visited[v]:
                dfs(v)
    
    dfs(start)
    return result

def count_connected_components(n, adj):
    """Count connected components"""
    visited = [False] * n
    count = 0
    
    def dfs(u):
        visited[u] = True
        for v in adj.get(u, []):
            if not visited[v]:
                dfs(v)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count

def has_cycle_undirected(n, adj):
    """Check cycle in undirected graph"""
    visited = [False] * n
    
    def dfs(u, parent):
        visited[u] = True
        
        for v in adj.get(u, []):
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False

# Usage:
print("Template 3: Graph Traversal")

adj = {0: [1, 2], 1: [2], 2: [3], 3: []}
print(f"BFS: {bfs_traversal(4, adj, 0)}")
print(f"DFS: {dfs_traversal(4, adj, 0)}")
