# Phase 11 - Graphs (Master Guide)

**Graphs appear in 25% of hard problems. Master traversal and algorithms.**

---

## Table of Contents
1. [Graph Fundamentals](#graph-fundamentals)
2. [Graph Representation](#graph-representation)
3. [BFS - Breadth First Search](#bfs-breadth-first-search)
4. [DFS - Depth First Search](#dfs-depth-first-search)
5. [Connected Components](#connected-components)
6. [Shortest Path Algorithms](#shortest-path-algorithms)
7. [Minimum Spanning Tree](#minimum-spanning-tree)
8. [Topological Sort](#topological-sort)
9. [Union-Find](#union-find)
10. [Worked Examples (40+)](#worked-examples)

---

# GRAPH FUNDAMENTALS

## Graph Definition

**Definition:** A graph G = (V, E) where:
- V = set of vertices (nodes)
- E = set of edges (connections)

**Types:**
```
Directed:   A → B (one direction)
Undirected: A ↔ B (both directions)
Weighted:   Edge has cost/distance
Cyclic:     Can return to starting vertex
Acyclic:    DAG (Directed Acyclic Graph)
```

---

# BFS - BREADTH FIRST SEARCH

```python
from collections import deque

def bfs(graph, start):
    """
    Level-by-level traversal
    Time: O(V + E)
    Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Example:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E']
```

---

# DFS - DEPTH FIRST SEARCH

## Recursive DFS

```python
def dfs_recursive(graph, node, visited, result):
    """
    Depth-first traversal (recursive)
    Time: O(V + E)
    Space: O(V) - recursion stack
    """
    visited.add(node)
    result.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

def dfs(graph, start):
    visited = set()
    result = []
    dfs_recursive(graph, start, visited, result)
    return result

print(dfs(graph, 'A'))  # ['A', 'B', 'D', 'C', 'E']
```

---

## Iterative DFS

```python
def dfs_iterative(graph, start):
    """
    DFS using explicit stack
    """
    visited = {start}
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node)
        
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    return result
```

---

# CONNECTED COMPONENTS

```python
def num_connected_components(n, edges):
    """
    Find number of connected components
    
    Time: O(V + E)
    Space: O(V)
    """
    graph = {i: [] for i in range(n)}
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    components = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1
    
    return components

# Example: 4 nodes, edges = [(0,1), (2,3)]
# Output: 2 (two components: {0,1} and {2,3})
```

---

# SHORTEST PATH ALGORITHMS

## Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph, start):
    """
    Find shortest paths from start to all nodes
    
    Precondition: No negative weights!
    Time: O((V + E) log V)
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]  # (distance, node)
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

## BFS for Shortest Path (Unweighted)

```python
def shortest_path_unweighted(graph, start, end):
    """
    For unweighted graphs, BFS finds shortest path
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

---

# TOPOLOGICAL SORT

```python
def topological_sort(graph):
    """
    Topological sort for DAG (Directed Acyclic Graph)
    
    Kahn's Algorithm (BFS-based)
    Time: O(V + E)
    Space: O(V)
    """
    in_degree = {node: 0 for node in graph}
    
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(graph):
        return None  # Cycle detected!
    
    return result

# Example: Course prerequisites
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

print(topological_sort(graph))  # [0, 1, 2, 3] or [0, 2, 1, 3]
```

---

# UNION-FIND (Disjoint Set Union)

```python
class UnionFind:
    """
    Efficient data structure for union and find operations
    
    Path compression: O(α(n)) ≈ O(1)
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compress path
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
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
    
    def connected(self, x, y):
        """Check if x and y are in same set"""
        return self.find(x) == self.find(y)

# Example:
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(uf.connected(0, 2))  # True
print(uf.connected(0, 3))  # False
```

---

# WORKED EXAMPLES

## Example 1: Number of Islands

```python
def numIslands(grid):
    """
    Count connected components of '1's
    
    Time: O(m × n)
    Space: O(m × n)
    """
    if not grid:
        return 0
    
    count = 0
    visited = set()
    
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or \
           (r, c) in visited or grid[r][c] == '0':
            return
        
        visited.add((r, c))
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    
    return count
```

---

## Example 2: Course Schedule (Cycle Detection)

```python
def canFinish(numCourses, prerequisites):
    """
    Check if all courses can be finished (no cycle)
    
    Time: O(V + E)
    Space: O(V)
    """
    graph = {i: [] for i in range(numCourses)}
    
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    visited = set()
    rec_stack = set()
    
    def has_cycle(node):
        if node in rec_stack:
            return True  # Cycle found
        
        if node in visited:
            return False  # Already processed
        
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        
        rec_stack.remove(node)
        return False
    
    for i in range(numCourses):
        if i not in visited and has_cycle(i):
            return False
    
    return True
```

---

**Master graphs. Hard problems often involve them.** 🎯

