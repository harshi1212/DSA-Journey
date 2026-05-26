# Problem Classification Guide

## Quick Pattern Recognition (5 Seconds)

When you see a problem, think:

---

## Problem Type → Algorithm Mapping

### String Problems

**Patterns to look for**:
- "Find substring..." → KMP, Z-algorithm, Rabin-Karp
- "Pattern matching..." → KMP
- "Palindrome..." → DP, expanding window
- "Anagram..." → Frequency counting, hashing

**Go-to algorithm**: Hash map (70% of string problems)

---

### Array Problems

**Patterns to look for**:
- "Sorted array..." → Binary search
- "Maximum/minimum..." → Dynamic programming, greedy
- "Subarray..." → Prefix sum, sliding window
- "Two sum..." → Hash map
- "Merge..." → Two pointers

**Go-to algorithm**: Hash map or two pointers

---

### Tree Problems

**Patterns to look for**:
- "Traverse..." → DFS/BFS
- "Sum path..." → DFS + backtracking
- "Lowest common ancestor..." → DFS + parent tracking
- "Balanced..." → Recursion
- "Serialize..." → DFS level order

**Go-to algorithm**: DFS recursion

---

### Graph Problems

**Patterns to look for**:
- "Connected components..." → Union-Find, DFS
- "Shortest path..." → Dijkstra, BFS
- "Topological..." → DFS, Kahn's
- "Strongly connected..." → Kosaraju, Tarjan
- "Bipartite..." → Graph coloring, BFS

**Go-to algorithm**: Depends on problem, start with DFS/BFS

---

### Dynamic Programming

**Patterns to look for**:
- "Maximum/minimum..." → DP
- "Count ways..." → DP
- "Can achieve..." → DP decision
- "Edit distance..." → DP
- "Longest..." → DP

**Go-to algorithm**: Think bottom-up DP

---

### Greedy Problems

**Patterns to look for**:
- "Maximum/minimum with choice..." → Greedy (verify locally optimal = globally)
- "Activity selection..." → Sort + greedy
- "Interval..." → Greedy (sort by end time)

**Go-to algorithm**: Sort + loop, try greedy choice

---

### Search Problems

**Patterns to look for**:
- "Find target..." → Binary search (if sorted) or hashing
- "Search in X..." → Understand X's structure
- "First/last occurrence..." → Binary search variants

**Go-to algorithm**: Binary search for sorted, hash for unsorted

---

## Decision Tree (30 Seconds)

```
Problem given
    ↓
Is it sorted?
    → Yes: Binary search?
    → No: Hash map? Sliding window? Two pointers?
    ↓
Single answer or multiple/path?
    → Single: Optimization (DP, greedy)
    → Multiple: Backtracking, DFS
    ↓
Tree structure?
    → Yes: DFS traversal
    → No:
    ↓
Graph structure?
    → Yes: DFS/BFS (or specialized: Dijkstra, Union-Find)
    → No:
    ↓
String/pattern?
    → Yes: KMP, hash, sliding window
    → No:
    ↓
Counting/ways?
    → Yes: DP or combinatorics
    → No:
    ↓
Hmm... think harder!
```

---

## Complexity Hints

| Time | Algorithm |
|------|-----------|
| O(1) | Constant lookup, math |
| O(log n) | Binary search |
| O(n) | Single pass, hash |
| O(n log n) | Sorting, heap |
| O(n²) | Nested loops, DP |
| O(n³) | Triple nested, interval DP |
| O(2^n) | Bitmask DP, backtracking |
| O(n!) | Permutations |

**Interview hint**: Better to start with O(n²), optimize to O(n log n)  
**Never**: Start with O(2^n) unless required

---

## Top 20 LeetCode Patterns

1. **Two Pointers** → Array/linked list movement
2. **Sliding Window** → Substring/subarray problems
3. **Binary Search** → Sorted data, decision
4. **DFS** → Trees, graphs, backtracking
5. **BFS** → Level-order, shortest path unweighted
6. **Hash Map** → Frequency, lookup, anagram
7. **Heap/Priority Queue** → K largest/smallest, Dijkstra
8. **Union-Find** → Connected components, MST
9. **DP** → Optimization, counting, sequences
10. **Greedy** → Sorting, choice problems
11. **Segment Tree** → Range queries
12. **Graph Coloring** → Bipartite checking
13. **Topological Sort** → Dependencies
14. **Dijkstra** → Shortest path weighted
15. **Backtracking** → Permutations, combinations
16. **Bit Manipulation** → XOR, bit flags
17. **String DP** → Edit distance, palindrome
18. **Math** → GCD, primes, combinatorics
19. **Simulation** → Follow the problem
20. **Divide and Conquer** → Merge sort, binary search

---

## Interview Strategy

```
Read problem (2 min)
    ↓
Recognize pattern (1 min)
    ↓
State algorithm (1 min)
    ↓
Code (15 min)
    ↓
Test (5 min)
    ↓
Optimize (3 min)
```

**Time for pattern recognition**: 1-3 min  
**Fastest wins**: Those who recognize patterns quickly
