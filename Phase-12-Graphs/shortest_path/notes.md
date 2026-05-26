# Shortest Path Algorithms

## The Problem

**Given**: Weighted graph, start node, end node  
**Find**: Shortest distance and path

---

## Algorithm Comparison

| Algorithm | Edge Weights | Negative Weights | Complexity |
|-----------|-------------|------------------|-----------|
| **BFS** | None (unweighted) | N/A | O(V+E) |
| **Dijkstra** | Positive | ✗ No | O(V²) or O(E log V) |
| **Bellman-Ford** | Positive/Negative | ✓ Yes | O(V·E) |
| **Floyd-Warshall** | Positive/Negative | ✓ Yes (no neg cycle) | O(V³) |

---

## Dijkstra's Algorithm

**How it works**:
1. Start with distance 0 for start node, infinity for others
2. Always visit nearest unvisited node
3. Update distances through this node
4. Repeat until all visited

**Greedy insight**: Once we visit a node, we've found the shortest path to it.

**Why it's brilliant**: Works for all positive edge weights!

**Example**:
```
     1
  A-----B
  |     |
 4|     |2
  |     |
  C-----D
     1

Shortest path A→D:
- Start: A (0)
- Visit A, update: B(1), C(4), D(∞)
- Visit B, update: D(3)
- Visit D, done!
- Path: A→B→D with distance 3
```

---

## When to use

- **Dijkstra**: Positive weights (GPS, routing)
- **Bellman-Ford**: Negative weights (currency exchange, anomaly detection)
- **Floyd-Warshall**: All pairs shortest path (small graphs <500 nodes)

---

## Implementation Notes

**Dijkstra**: Use min-heap for efficiency  
**Bellman-Ford**: Relax edges V-1 times  
**Floyd-Warshall**: 3 nested loops for all pairs
