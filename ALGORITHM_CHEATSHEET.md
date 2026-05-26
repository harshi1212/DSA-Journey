# Algorithm Cheatsheet - Quick Reference

**Use this**: 5 minutes before coding in an interview  
**Print this**: Keep at desk during practice sessions

---

## Core Algorithms by Category

### **SEARCHING**

| Algorithm | Time (Best/Avg/Worst) | Space | Key Idea | When |
|-----------|----------------------|-------|----------|------|
| Linear Search | O(1)/O(n)/O(n) | O(1) | Check each element | Unsorted data |
| Binary Search | O(1)/O(log n)/O(log n) | O(1) | Divide and conquer | Sorted data ⭐ |
| Binary Search (variants) | O(log n) | O(1) | Find first/last/insert pos | Boundary problems |

---

### **SORTING**

| Algorithm | Time (Best/Avg/Worst) | Space | Stable | When |
|-----------|----------------------|-------|--------|------|
| Bubble Sort | O(n)/O(n²)/O(n²) | O(1) | Yes | Learning only |
| Insertion Sort | O(n)/O(n²)/O(n²) | O(1) | Yes | Small arrays |
| Merge Sort | O(n log n)/O(n log n)/O(n log n) | O(n) | Yes | When stable + O(n log n) needed ⭐ |
| Quick Sort | O(n log n)/O(n log n)/O(n²) | O(log n) | No | General sorting ⭐ |
| Heap Sort | O(n log n)/O(n log n)/O(n log n) | O(1) | No | In-place needed |
| Counting Sort | O(n+k) | O(k) | Yes | Small range integers |
| Radix Sort | O(nk) | O(n+k) | Yes | Non-comparative |

---

### **ARRAYS & STRINGS**

| Problem Type | Algorithm | Time | Space | Pattern |
|--------------|-----------|------|-------|---------|
| Two pointers | Two pointers | O(n) | O(1) | Opposite ends |
| Sliding window | Window + hash | O(n) | O(k) | Substring/subarray |
| Subarray sum | Prefix sum | O(n) | O(n) | Contiguous sum |
| Find target | Hash map | O(n) | O(n) | Quick lookup ⭐ |
| Merge sorted | Two pointers | O(n) | O(n) | Compare heads |
| Pattern match | KMP | O(n+m) | O(m) | Substring search |
| Multiple patterns | Rabin-Karp | O(n+m) | O(1) | Hash comparison |

---

### **DYNAMIC PROGRAMMING**

| Type | State | Time | Space | Example |
|------|-------|------|-------|---------|
| 1D DP | dp[i] | O(n) | O(n) | Fibonacci, climb stairs |
| 2D DP | dp[i][j] | O(n²) | O(n²) | Knapsack, LCS |
| Interval DP | dp[i][j] | O(n³) | O(n²) | Burst balloons |
| Bitmask DP | dp[mask][i] | O(2^n * n) | O(2^n * n) | TSP (n ≤ 20) |
| Tree DP | dp[node][state] | O(n) | O(n) | House robber III |
| Digit DP | dp[pos][tight] | O(10 * log n) | O(10 * log n) | Count digit one |

**Transition**: dp[i] = function of dp[i-1], dp[i-2], ...

---

### **GRAPHS**

| Problem | Algorithm | Time | Space | Finds |
|---------|-----------|------|-------|-------|
| Connected components | DFS/BFS | O(V+E) | O(V) | All components |
| Shortest path (unweighted) | BFS | O(V+E) | O(V) | Shortest unweighted |
| Shortest path (weighted) | Dijkstra | O((V+E)log V) | O(V) | Shortest from one source |
| All pairs shortest | Floyd-Warshall | O(V³) | O(V²) | All pairs |
| Topological sort | DFS/Kahn | O(V+E) | O(V) | Dependency order |
| Strongly connected | Kosaraju/Tarjan | O(V+E) | O(V) | SCCs |
| Minimum spanning tree | Kruskal | O(E log E) | O(V) | MST ⭐ |
| Minimum spanning tree | Prim | O(E log V) | O(V) | MST |
| Bipartite check | Graph coloring | O(V+E) | O(V) | 2-colorable |
| Articulation points | DFS + low-link | O(V+E) | O(V) | Cut vertices |

---

### **HEAPS & PRIORITY QUEUES**

| Operation | Time | Use |
|-----------|------|-----|
| Insert | O(log n) | Add to priority queue |
| Delete min/max | O(log n) | Get next priority item |
| Build heap | O(n) | Create from array |
| Find k largest | O(n log k) | K heap + min-heap |
| Find k smallest | O(n log k) | K heap + max-heap |

---

### **HASH TABLES & MAPS**

| Operation | Average | Worst | Use |
|-----------|---------|-------|-----|
| Insert | O(1) | O(n) | Add key-value |
| Delete | O(1) | O(n) | Remove key |
| Lookup | O(1) | O(n) | Get value by key ⭐ |
| Collision resolution | - | - | Chaining or open addressing |

**When to use hash map**: Need fast lookup, frequency counting, two-sum problems

---

### **TREES**

| Traversal | Order | Use | Time |
|-----------|-------|-----|------|
| Inorder | Left-Root-Right | BST sorted order | O(n) |
| Preorder | Root-Left-Right | Copy tree | O(n) |
| Postorder | Left-Right-Root | Delete tree | O(n) |
| Level order | By level | BFS | O(n) |

| Operation | Time (BST) | Space |
|-----------|-----------|-------|
| Search | O(log n) avg, O(n) worst | O(log n) recursion |
| Insert | O(log n) avg, O(n) worst | O(log n) recursion |
| Delete | O(log n) avg, O(n) worst | O(log n) recursion |
| Balance (AVL) | O(log n) | O(log n) |

---

### **UNION-FIND (DISJOINT SET UNION)**

| Operation | Time (with path compression + union by rank) |
|-----------|----------------------------------------------|
| Find | O(α(n)) ≈ O(1) |
| Union | O(α(n)) ≈ O(1) |

**When**: Connected components, cycle detection, MST (Kruskal's)

---

### **SEGMENT TREE**

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n) | O(n) |
| Query (range) | O(log n) | O(log n) recursion |
| Update (point) | O(log n) | O(log n) recursion |

**When**: Range sum/min/max queries with updates

---

### **FENWICK TREE (BINARY INDEXED TREE)**

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n) | O(n) |
| Query (prefix sum) | O(log n) | O(1) recursion |
| Update (point) | O(log n) | O(1) recursion |

**When**: Prefix sum queries with point updates

---

### **TRIE**

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| Prefix search | O(m) | O(1) |

**When**: Autocomplete, spell checker, IP routing (m = word length)

---

### **GREEDY**

| Problem | Algorithm | Time | Greedy Choice |
|---------|-----------|------|----------------|
| Activity selection | Sort by end time | O(n log n) | Pick earliest ending |
| Huffman coding | Min-heap | O(n log n) | Merge smallest freq |
| Coin change (greedy) | Sort & pick | O(n) | Largest coin first (depends on coins) |
| Jump game | Greedy scan | O(n) | Max reach forward |
| Gas station | One pass | O(n) | Start where surplus |

**When**: Locally optimal = globally optimal (verify before using!)

---

## **COMPLEXITY CHEAT SHEET**

| Notation | Operations per second (n=1M) |
|----------|------------------------------|
| O(1) | 1,000,000,000 ✓ |
| O(log n) | ~20 ✓ |
| O(n) | 1,000,000 ✓ |
| O(n log n) | ~20,000,000 ✓ |
| O(n²) | 1,000,000,000,000 ✗ |
| O(2^n) | Impossible |

**Rule**: Aim for O(n log n) or better for n ≤ 10^6

---

## **COMMON PATTERNS**

| Pattern | Problem Type | Time | Approach |
|---------|--------------|------|----------|
| **Two Pointers** | Palindrome, sorted array | O(n) | Start opposite ends |
| **Sliding Window** | Substring, subarray | O(n) | Window + hash |
| **Binary Search** | Sorted + decision | O(log n) | Divide range |
| **DFS/Recursion** | Trees, permutations | O(branching^depth) | Explore all paths |
| **BFS** | Shortest path, levels | O(V+E) | Queue based |
| **DP** | Optimization, counting | Varies | Memoization |
| **Hash Map** | Lookup, frequency | O(n) | Quick reference |
| **Heap** | K largest/smallest | O(n log k) | Priority queue |

---

## **QUICK DECISION TREE**

```
Problem?
├─ Sorted data?
│  └─ Binary search (O(log n)) ✓
├─ Need frequency?
│  └─ Hash map (O(n)) ✓
├─ Tree/Graph?
│  └─ DFS/BFS (O(V+E)) ✓
├─ Optimization?
│  ├─ Greedy? → Verify locally optimal
│  └─ DP? → Define states ✓
├─ String pattern?
│  └─ KMP or Rabin-Karp ✓
└─ Else?
   └─ Think... brute force first!
```

---

## **COMPLEXITY ANALYSIS TEMPLATE**

When analyzing algorithm:

```
Time Complexity:
- Outer loop: O(n)
- Inner loop: O(m)
- Hash lookup: O(1)
- Total: O(n * m)

Space Complexity:
- Hash map: O(n)
- Recursion depth: O(log n)
- Total: O(n)
```

---

## **KEY INSIGHTS**

1. **Hash map is powerful** - Solves 70% of array problems
2. **Two pointers works** - Sorted data often has two-pointer solution
3. **DFS > recursion** - For trees and graphs, think DFS
4. **Sort first** - Sorting enables many algorithms (O(n log n) often worth it)
5. **DP is optimization** - When greedy doesn't work, try DP
6. **Preprocess data** - Building hash/segment tree pays off
7. **Space-time trade-off** - More space often means faster time

---

## **BEFORE EACH INTERVIEW**

Print and review:
- [ ] This cheatsheet (5 min)
- [ ] Your weakest algorithm (2 min)
- [ ] One complete code template (3 min)
- [ ] One mock problem (10 min)

**Total**: 20 minutes of focused prep = 30% improvement
