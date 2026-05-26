# Phase 16 - Advanced Graph Algorithms

## What Advanced Topics?

When basic BFS/DFS aren't enough:

| Problem | Algorithm | Complexity |
|---------|-----------|-----------|
| **Minimum spanning tree** | Kruskal's, Prim's | O(E log V) |
| **Strongly connected components** | Kosaraju, Tarjan | O(V+E) |
| **Bipartite checking** | DFS/BFS coloring | O(V+E) |
| **Articulation points** | DFS + low-link | O(V+E) |

---

## Minimum Spanning Tree (MST)

**What**: Subset of edges connecting all vertices with minimum total weight

**Why**: Minimum cost network (electrical grid, road network, etc.)

**Algorithms**:
- **Kruskal's**: Sort edges, use Union-Find (O(E log E))
- **Prim's**: Grow tree with min-heap (O(E log V))

---

## Strongly Connected Components (SCC)

**What**: Maximal subgraphs where every vertex reaches every other

**Why**: Social networks (find cliques), software dependencies

**Algorithms**:
- **Kosaraju's**: 2 DFS passes (O(V+E))
- **Tarjan's**: 1 DFS with stack (O(V+E))

---

## Bipartite Checking

**What**: Can color vertices with 2 colors such no adjacent vertices same color?

**Why**: Job scheduling, matching problems, checkerboard patterns

**Algorithm**: BFS/DFS coloring (O(V+E))

---

## When You Need Advanced Graph

- **Hard problems**: Usually need advanced techniques
- **Large graphs**: Optimization matters
- **Real systems**: Networks, social graphs, dependency graphs
