"""
Topological Sort
Linear ordering of vertices in a Directed Acyclic Graph (DAG).
"""

def topological_sort_dfs(graph, num_nodes):
    """
    Topological sort using DFS.
    Only works for DAGs (Directed Acyclic Graphs).
    """
    visited = [False] * (num_nodes + 1)
    stack = []
    
    def dfs(node):
        visited[node] = True
        
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
        
        # Add to stack after visiting all neighbors
        stack.append(node)
    
    # Visit all nodes
    for node in range(1, num_nodes + 1):
        if not visited[node]:
            dfs(node)
    
    # Reverse to get topological order
    return stack[::-1]

def topological_sort_kahn(graph, num_nodes):
    """
    Topological sort using Kahn's algorithm (BFS-based).
    Also detects cycles.
    """
    # Calculate in-degrees
    in_degree = [0] * (num_nodes + 1)
    for node in range(1, num_nodes + 1):
        for neighbor in graph.get(node, []):
            in_degree[neighbor] += 1
    
    # Queue of nodes with in-degree 0
    queue = [node for node in range(1, num_nodes + 1) if in_degree[node] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        # Remove edge to neighbors
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If not all nodes processed, graph has cycle
    if len(result) != num_nodes:
        return None  # Cycle detected
    
    return result

# Example 1: Course prerequisites
print("=== Course Prerequisites ===")
# Edge: A→B means "take A before B"
courses = {
    1: [2, 3],      # Intro Math → Calculus, Physics
    2: [4],         # Calculus → Advanced Calc
    3: [4],         # Physics → Advanced Physics
    4: [],          # Advanced Calc/Physics (no prerequisites)
}

order = topological_sort_dfs(courses, 4)
print(f"Course order: {' → '.join(map(str, order))}")
# Output: 1 → 2 → 3 → 4 (or 1 → 3 → 2 → 4, both valid)

# Example 2: Task dependencies
print("\n=== Task Scheduling ===")
tasks = {
    'A': ['B', 'C'],     # A must complete before B, C
    'B': ['D'],          # B before D
    'C': ['D'],          # C before D
    'D': [],             # D is final task
}

# Convert to numbers for algorithm
task_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
reverse_map = {v: k for k, v in task_map.items()}

numeric_tasks = {}
for task, deps in tasks.items():
    numeric_tasks[task_map[task]] = [task_map[d] for d in deps]

order = topological_sort_kahn(numeric_tasks, 4)
if order:
    order_str = ' → '.join(reverse_map[node] for node in order)
    print(f"Task order: {order_str}")
else:
    print("Cycle detected!")

# Example 3: Cycle detection
print("\n=== Cycle Detection ===")
cyclic_graph = {
    1: [2],
    2: [3],
    3: [1],  # Creates cycle: 1→2→3→1
}

order = topological_sort_kahn(cyclic_graph, 3)
if order:
    print(f"Topological order: {order}")
else:
    print("Graph has cycle - cannot sort")

# Example 4: Build system dependencies
print("\n=== Build System ===")
# package.json style dependencies:
# utils.js: no dependencies
# helpers.js: depends on utils.js
# app.js: depends on helpers.js, utils.js

dependencies = {
    'utils': [],
    'helpers': ['utils'],
    'app': ['helpers', 'utils'],
}

# Convert to numbers
files = list(dependencies.keys())
file_map = {f: i+1 for i, f in enumerate(files)}
reverse_file_map = {v: k for k, v in file_map.items()}

numeric_deps = {}
for file, deps in dependencies.items():
    numeric_deps[file_map[file]] = [file_map[d] for d in deps]

order = topological_sort_kahn(numeric_deps, len(files))
if order:
    build_order = ' → '.join(reverse_file_map[node] for node in order)
    print(f"Build order: {build_order}")
else:
    print("Circular dependency!")

print("\n=== Complexity Analysis ===")
print("Time:  O(V + E) - both algorithms")
print("Space: O(V) - stack or queue")
print("\nUse Kahn's algorithm to detect cycles")
