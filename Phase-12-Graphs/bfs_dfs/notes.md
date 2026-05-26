# BFS & DFS - Graph Traversal

## BFS (Breadth-First Search)

**What**: Explore neighbors level by level.

**How**: Use a Queue.

**Step by step**:
```
Start at node 1
Queue: [1]
Visit 1, add neighbors [2, 3]
Queue: [2, 3]
Visit 2, add neighbors [4]
Queue: [3, 4]
Visit 3, no new neighbors
Queue: [4]
Visit 4
Queue: []
```

**When to use**:
- Shortest path in unweighted graph
- Level-order traversal
- Connected components
- Bipartite checking

**Complexity**: O(V + E) - visit each vertex and edge once

---

## DFS (Depth-First Search)

**What**: Explore deeply before backtracking.

**How**: Use a Stack or recursion.

**Step by step**:
```
Start at 1
Stack: [1]
Visit 1, add 2
Stack: [2]
Visit 2, add 4
Stack: [4]
Visit 4, no neighbors
Stack: []
Backtrack, add 3
Stack: [3]
Visit 3
Stack: []
```

**When to use**:
- Cycle detection
- Topological sort
- Path finding
- Connected components

**Complexity**: O(V + E) - same as BFS

---

## Comparison

| Feature | BFS | DFS |
|---------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Order | Level by level | Branch by branch |
| Shortest Path | ✓ (unweighted) | ✗ |
| Cycle Detection | ✓ | ✓ |
| Memory | More (all level) | Less (one path) |
| Use Case | Shortest path | Connectivity |

---

## Implementation Tips

**Both need**:
- Visited set (don't revisit)
- Start node
- Adjacency list (graph representation)

**Common mistakes**:
1. Forgetting to mark visited → infinite loop
2. Wrong data structure (stack vs queue)
3. Not handling disconnected components
