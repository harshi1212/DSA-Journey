"""
DFS - Depth-First Search
Use recursion or Stack (LIFO) to explore deeply.
"""

def dfs_recursive(graph, node, visited, result):
    """DFS using recursion."""
    visited.add(node)
    result.append(node)
    
    # Visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

def dfs_iterative(graph, start):
    """DFS using stack."""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()  # Pop from end (LIFO)
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors (reverse order for consistent results)
            stack.extend(reversed(graph[node]))
    
    return result

# Example 1: DFS traversal
print("=== DFS Traversal ===")
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

visited = set()
result = []
dfs_recursive(graph, 1, visited, result)
print(f"DFS from 1 (recursive): {result}")  # [1, 2, 4, 3, 5]

result_iter = dfs_iterative(graph, 1)
print(f"DFS from 1 (iterative): {result_iter}")  # Similar order

# Example 2: Cycle detection
def has_cycle_dfs(graph, num_nodes):
    """Detect cycle in directed graph."""
    # States: 0 = white (unvisited), 1 = gray (visiting), 2 = black (visited)
    state = [0] * (num_nodes + 1)
    
    def dfs(node):
        state[node] = 1  # Mark as visiting (gray)
        
        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:  # Back edge = cycle
                return True
            if state[neighbor] == 0 and dfs(neighbor):
                return True
        
        state[node] = 2  # Mark as visited (black)
        return False
    
    # Check from each node
    for node in range(1, num_nodes + 1):
        if state[node] == 0:
            if dfs(node):
                return True
    
    return False

print("\n=== Cycle Detection ===")
# Directed graph with cycle: 1→2→3→1
cyclic_graph = {
    1: [2],
    2: [3],
    3: [1],
    4: []
}
has_cycle = has_cycle_dfs(cyclic_graph, 4)
print(f"Graph has cycle: {has_cycle}")  # True

# Acyclic graph
acyclic_graph = {
    1: [2],
    2: [3],
    3: [],
    4: []
}
has_cycle = has_cycle_dfs(acyclic_graph, 4)
print(f"DAG has cycle: {has_cycle}")  # False

# Example 3: All paths
def all_paths(graph, start, end, path=[]):
    """Find all paths from start to end."""
    path = path + [start]
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph.get(start, []):
        new_paths = all_paths(graph, neighbor, end, path)
        paths.extend(new_paths)
    
    return paths

print("\n=== All Paths ===")
simple_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
paths = all_paths(simple_graph, 'A', 'D')
print(f"Paths A→D: {paths}")  # [['A','B','D'], ['A','C','D']]

print("\n=== Complexity ===")
print("Time:  O(V + E) - same as BFS")
print("Space: O(V) - recursion stack or explicit stack")
