"""
Connected Components using DFS/BFS
Find all connected groups in a graph.
"""

from collections import deque

def count_components_dfs(graph, num_nodes):
    """Count connected components using DFS."""
    visited = [False] * (num_nodes + 1)
    count = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
    
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            dfs(node)
            count += 1
    
    return count

def count_components_bfs(graph, num_nodes):
    """Count connected components using BFS."""
    visited = [False] * (num_nodes + 1)
    count = 0
    
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            # BFS from this node
            queue = deque([node])
            visited[node] = True
            
            while queue:
                curr = queue.popleft()
                for neighbor in graph.get(curr, []):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            count += 1
    
    return count

def find_components(graph, num_nodes):
    """Find all connected components."""
    visited = [False] * (num_nodes + 1)
    components = []
    
    def dfs(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor, component)
    
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            component = []
            dfs(node, component)
            components.append(component)
    
    return components

# Example 1: Disconnected graph
print("=== Connected Components ===\n")

graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4, 6],
    6: [5],
}

count = count_components_dfs(graph, 6)
print(f"Number of components: {count}")  # 2

components = find_components(graph, 6)
print(f"Components: {components}")  # [[1,2,3], [4,5,6]]

# Example 2: Number of Islands (2D grid)
def num_islands(grid):
    """
    Count number of islands in a 2D grid.
    1 = land, 0 = water
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or grid[r][c] == 0:
            return
        
        visited[r][c] = True
        # Check 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                count += 1
    
    return count

print("\n=== Number of Islands ===")
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]

islands = num_islands(grid)
print(f"Grid:\n{chr(10).join(str(row) for row in grid)}")
print(f"Number of islands: {islands}")  # 3

# Example 3: Largest component
def largest_component(graph, num_nodes):
    """Find size of largest connected component."""
    visited = [False] * (num_nodes + 1)
    max_size = 0
    
    def dfs(node):
        visited[node] = True
        size = 1
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                size += dfs(neighbor)
        return size
    
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            component_size = dfs(node)
            max_size = max(max_size, component_size)
    
    return max_size

print("\n=== Largest Component ===")
size = largest_component(graph, 6)
print(f"Largest component size: {size}")  # 3

print("\n=== Complexity ===")
print("Time:  O(V + E) - visit each vertex and edge once")
print("Space: O(V) - visited array and recursion stack")
