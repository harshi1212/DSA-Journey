# Connected Components

## What are Connected Components?

Groups of nodes that are connected together.

**Visual**:
```
1 -- 2      4 -- 5
|    |      |    |
3 ---       6 ---

Component 1: {1, 2, 3}
Component 2: {4, 5, 6}
```

---

## Two Algorithms

| Algorithm | Data Structure | Best For | Complexity |
|-----------|----------------|----------|-----------|
| **DFS/BFS** | Graph | Small graphs, simple problems | O(V+E) |
| **Union-Find** | Disjoint Set Union | Dynamic connectivity, large graphs | Nearly O(1) per operation |

---

## When You Need This

- Social networks: Group friends by connected community
- Network connectivity: Which servers are unreachable?
- Graph coloring: How many colors needed?
- Island detection: Count separate islands

---

## Problems This Solves

1. **Number of Islands**: Count separate land areas
2. **Friends Circle**: How many friend groups?
3. **Largest Component**: Biggest connected group?
4. **Graph Connectivity**: Is graph connected?
