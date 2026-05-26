"""
Bipartite Graph Check and Coloring
A graph is bipartite if vertices can be colored with 2 colors
such that no adjacent vertices have same color
"""

from collections import deque

def is_bipartite_bfs(n, edges):
    """
    Check if graph is bipartite using BFS coloring.
    Colors: -1 (uncolored), 0 (color 1), 1 (color 2)
    """
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        
        # BFS from uncolored node
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            
            for v in edges.get(u, []):
                if color[v] == -1:
                    color[v] = 1 - color[u]  # Opposite color
                    queue.append(v)
                elif color[v] == color[u]:
                    # Same color for adjacent vertices = not bipartite
                    return False
    
    return True

def is_bipartite_dfs(n, edges):
    """Check bipartite using DFS."""
    color = [-1] * n
    
    def dfs(u, c):
        color[u] = c
        for v in edges.get(u, []):
            if color[v] == -1:
                if not dfs(v, 1 - c):
                    return False
            elif color[v] == color[u]:
                return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    
    return True

def get_bipartition(n, edges):
    """Get actual partition if graph is bipartite."""
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            for v in edges.get(u, []):
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return None  # Not bipartite
    
    partition1 = [i for i in range(n) if color[i] == 0]
    partition2 = [i for i in range(n) if color[i] == 1]
    
    return partition1, partition2

# Example 1: Simple bipartite graph
print("=== Bipartite Checking ===\n")

# Bipartite: 0-1-2-3, arranged as 0-2 on one side, 1-3 on other
n = 4
edges = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2],
}

print("Graph edges:")
for u in edges:
    for v in edges[u]:
        print(f"  {u} - {v}")

is_bip = is_bipartite_bfs(n, edges)
print(f"\nIs bipartite? {is_bip}")

if is_bip:
    partition = get_bipartition(n, edges)
    print(f"Partitions: {partition}")

# Example 2: Non-bipartite (triangle)
print("\n=== Non-Bipartite Graph ===\n")

n = 3
triangle = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
}

print("Triangle edges:")
for u in triangle:
    for v in triangle[u]:
        print(f"  {u} - {v}")

is_bip = is_bipartite_bfs(n, triangle)
print(f"\nIs bipartite? {is_bip}")

# Example 3: Real-world - job assignment
print("\n=== Real-World: Job Assignment ===\n")

people = ['Alice', 'Bob', 'Carol']
jobs = ['Job1', 'Job2', 'Job3']

# Can assign: Alice→Job1, Alice→Job2, Bob→Job2, Carol→Job3
# This is bipartite: people on one side, jobs on other
n = 6  # 3 people + 3 jobs
edges = {
    0: [3, 4],      # Alice can do Job1, Job2
    1: [4, 5],      # Bob can do Job2, Job3
    2: [5],         # Carol can do Job3
    3: [0],         # Job1 needs Alice
    4: [0, 1],      # Job2 needs Alice or Bob
    5: [1, 2],      # Job3 needs Bob or Carol
}

print("People (0-2): Alice, Bob, Carol")
print("Jobs (3-5): Job1, Job2, Job3")
print("\nAssignments (edges between people and jobs):")
for u in range(3):
    person = ['Alice', 'Bob', 'Carol'][u]
    job_list = [f"Job{edges[u][i]-2}" for i in range(len(edges[u]))]
    print(f"  {person}: {job_list}")

is_bip = is_bipartite_bfs(n, edges)
print(f"\nIs bipartite? {is_bip} (should be True)")

# Example 4: Checkerboard pattern
print("\n=== Checkerboard Pattern ===\n")

# 2x2 checkerboard
grid = [
    ['W', 'B'],
    ['B', 'W'],
]

# Convert to graph: adjacent cells have edges
n = 4
edges_board = {
    0: [1, 2],      # (0,0) white adjacent to (0,1), (1,0)
    1: [0, 3],      # (0,1) black adjacent to (0,0), (1,1)
    2: [0, 3],      # (1,0) black adjacent to (0,0), (1,1)
    3: [1, 2],      # (1,1) white adjacent to (0,1), (1,0)
}

print("Checkerboard (adjacent cells connected):")
for row in grid:
    print("  " + " ".join(row))

is_bip = is_bipartite_bfs(n, edges_board)
print(f"\nIs bipartite? {is_bip} (should be True)")

partition = get_bipartition(n, edges_board)
print(f"White cells: {partition[0]}")
print(f"Black cells: {partition[1]}")

print("\n=== Complexity ===")
print("BFS/DFS:  O(V + E) - visit each vertex and edge once")
print("Space:    O(V) - color array")
print("\nBipartite = 2-colorable = no odd cycles")
