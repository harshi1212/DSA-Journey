"""
BFS - Breadth-First Search
Use Queue (FIFO) to explore level by level.
"""

from collections import deque

def bfs(graph, start):
    """
    BFS traversal from start node.
    
    Args:
        graph: dict {node: [neighbors]}
        start: starting node
    
    Returns:
        list of nodes in BFS order
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()  # Pop from front (FIFO)
        result.append(node)
        
        # Add unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Example 1: Simple graph traversal
print("=== BFS Traversal ===")
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

print(f"Graph: {graph}")
result = bfs(graph, 1)
print(f"BFS from 1: {result}")  # [1, 2, 3, 4, 5]

# Example 2: Shortest path
def bfs_shortest_path(graph, start, end):
    """Find shortest path from start to end."""
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])  # (node, path)
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []

print("\n=== Shortest Path ===")
path = bfs_shortest_path(graph, 1, 5)
print(f"Shortest path 1→5: {path}")  # [1, 3, 5]

# Example 3: Connected components
def count_components(graph, nodes):
    """Count number of connected components."""
    visited = set()
    components = 0
    
    for node in nodes:
        if node not in visited:
            # BFS from unvisited node
            queue = deque([node])
            visited.add(node)
            
            while queue:
                curr = queue.popleft()
                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            components += 1
    
    return components

print("\n=== Connected Components ===")
disconnected_graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}
components = count_components(disconnected_graph, [1, 2, 3, 4, 5])
print(f"Components: {components}")  # 3

print("\n=== Complexity ===")
print("Time:  O(V + E) - visit each vertex once, traverse each edge")
print("Space: O(V) - queue and visited set")
