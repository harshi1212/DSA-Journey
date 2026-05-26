"""
Strongly Connected Components (SCC)
Find all maximal strongly connected subgraphs
"""

def kosaraju_scc(n, adj):
    """
    Find SCC using Kosaraju's algorithm.
    
    Algorithm:
    1. DFS on original graph, store order by finish time
    2. DFS on transposed graph in reverse order
    3. Each tree = one SCC
    """
    # Step 1: DFS to get finish order
    visited = [False] * n
    finish_order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj.get(u, []):
            if not visited[v]:
                dfs1(v)
        finish_order.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    # Step 2: Build transposed graph
    transpose = {i: [] for i in range(n)}
    for u in adj:
        for v in adj[u]:
            transpose[v].append(u)
    
    # Step 3: DFS on transpose in reverse finish order
    visited = [False] * n
    sccs = []
    
    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in transpose.get(u, []):
            if not visited[v]:
                dfs2(v, component)
    
    for u in reversed(finish_order):
        if not visited[u]:
            component = []
            dfs2(u, component)
            sccs.append(component)
    
    return sccs

def tarjan_scc(n, adj):
    """
    Find SCC using Tarjan's algorithm.
    Single DFS with stack and low-link values.
    """
    index_counter = [0]
    stack = []
    lowlinks = [0] * n
    index = [0] * n
    on_stack = [False] * n
    index_initialized = [False] * n
    sccs = []
    
    def strongconnect(v):
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        index_initialized[v] = True
        stack.append(v)
        on_stack[v] = True
        
        for w in adj.get(v, []):
            if not index_initialized[w]:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif on_stack[w]:
                lowlinks[v] = min(lowlinks[v], index[w])
        
        if lowlinks[v] == index[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            sccs.append(component)
    
    for v in range(n):
        if not index_initialized[v]:
            strongconnect(v)
    
    return sccs

# Example 1: Kosaraju's Algorithm
print("=== Strongly Connected Components ===\n")

# Create directed graph: 0→1→2→0 (cycle), 1→3
n = 4
adj = {
    0: [1],
    1: [2, 3],
    2: [0],
    3: [],
}

print("Directed graph:")
for u in adj:
    for v in adj[u]:
        print(f"  {u} → {v}")

sccs = kosaraju_scc(n, adj)

print(f"\nStrongly Connected Components:")
for i, scc in enumerate(sccs):
    print(f"  Component {i+1}: {scc}")

# Example 2: Tarjan's Algorithm
print("\n=== Tarjan's SCC ===\n")

sccs_tarjan = tarjan_scc(n, adj)
print(f"Tarjan's result:")
for i, scc in enumerate(sccs_tarjan):
    print(f"  Component {i+1}: {scc}")

# Example 3: Software dependency graph
print("\n=== Real-World: Software Dependencies ===\n")

modules = ['main', 'util', 'parser', 'compiler']
n = len(modules)

# Dependencies: module[i] depends on module[j]
dependencies = {
    0: [1, 2],           # main depends on util, parser
    1: [],               # util has no dependencies
    2: [1, 3],           # parser depends on util, compiler
    3: [1],              # compiler depends on util
}

print("Modules:", modules)
print("Dependencies:")
for i, deps in dependencies.items():
    print(f"  {modules[i]} depends on: {[modules[j] for j in deps]}")

sccs = kosaraju_scc(n, dependencies)

print(f"\nCircular dependencies (if any):")
has_cycle = False
for scc in sccs:
    if len(scc) > 1:
        print(f"  Cycle found: {[modules[i] for i in scc]}")
        has_cycle = True

if not has_cycle:
    print("  No cycles - dependency graph is valid!")

# Example 4: Complex graph with multiple cycles
print("\n=== Complex Graph ===\n")

n = 6
# Graph with cycles: 0-1-2-0 and 3-4-5-3
adj_complex = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3],
}

print("Graph edges:")
for u in adj_complex:
    for v in adj_complex[u]:
        print(f"  {u} → {v}")

sccs = kosaraju_scc(n, adj_complex)

print(f"\nSCCs found: {len(sccs)}")
for scc in sccs:
    print(f"  {scc}")

print("\n=== Complexity ===")
print("Kosaraju:  O(V + E) - two DFS passes")
print("Tarjan:    O(V + E) - single DFS")
print("Both:      Linear in graph size")
print("\nKosaraju: Easier to understand")
print("Tarjan:   Slightly more efficient (1 pass)")
