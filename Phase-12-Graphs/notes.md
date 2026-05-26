# Phase 12 - Graph Algorithms

## What is a Graph?

A graph is a collection of nodes (vertices) connected by edges.

**Visual**:
```
    1 --- 2
    |     |
    3 --- 4
```

Nodes: 1, 2, 3, 4  
Edges: (1-2), (1-3), (2-4), (3-4)

---

## Two Types of Graphs

### 1. **Undirected Graph** (edges go both ways)
```
1 --- 2    means 1↔2
```

### 2. **Directed Graph** (edges have direction)
```
1 → 2    means 1→2 (not 2→1)
```

---

## Master These 4 Algorithms

| Algorithm | What It Does | Use Case | Complexity |
|-----------|-------------|----------|-----------|
| **BFS** | Explore by level (breadth) | Shortest path in unweighted | O(V+E) |
| **DFS** | Explore deeply (depth) | Cycle detection, connectivity | O(V+E) |
| **Dijkstra** | Shortest path (weighted) | GPS navigation, routing | O(V²) or O(E log V) |
| **Topological Sort** | Linear ordering of DAG | Task scheduling, build order | O(V+E) |

---

## Real-World Examples

**BFS**:
- Level-order traversal (Facebook: friends → 2nd degree → 3rd degree)
- Shortest path in maze

**DFS**:
- All friends of a person (depth exploration)
- Detect cycles (deadlock detection)

**Dijkstra**:
- Google Maps (shortest route)
- Network routing

**Topological Sort**:
- Course prerequisites (take math before physics)
- Build dependencies

---

## Key Concepts

### **Representation**:
1. **Adjacency List** (preferred) - Save space, iterate neighbors easily
2. **Adjacency Matrix** - Dense graphs, fast lookup

### **Traversal Strategy**:
- **BFS**: Use Queue (FIFO)
- **DFS**: Use Stack (LIFO) or recursion

### **Distance**:
- **Unweighted**: Count edges (use BFS)
- **Weighted**: Calculate path weight (use Dijkstra)

---

## Practice by Algorithm

All algorithms have example problems in their folders.
