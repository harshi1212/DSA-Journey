# LeetCode Problem Mapping

**Using LeetCode problems mapped to each phase of this curriculum**

Use this to find problems that match your current learning level.

---

## **Phase 0-1: Python Basics & Fundamentals**

**Focus**: Syntax, loops, basic problem solving

### Easy (Start Here)
1. **Two Sum** (1) - Hash map basics
   - [Problem](https://leetcode.com/problems/two-sum/)
   - Pattern: Hash map
   - Time: O(n), Space: O(n)
   - Solution approach: One pass with hash

2. **Palindrome Number** (9) - Math basics
   - [Problem](https://leetcode.com/problems/palindrome-number/)
   - Pattern: Math
   - Time: O(log n)

3. **Valid Parentheses** (20) - Stack basics
   - [Problem](https://leetcode.com/problems/valid-parentheses/)
   - Pattern: Stack
   - Time: O(n)

4. **Merge Two Sorted Lists** (21) - Linked list basics
   - [Problem](https://leetcode.com/problems/merge-two-sorted-lists/)
   - Pattern: Two pointers
   - Time: O(n+m)

5. **Roman to Integer** (13) - Hash map
   - [Problem](https://leetcode.com/problems/roman-to-integer/)
   - Pattern: Hash map
   - Time: O(n)

---

## **Phase 2-3: OOP & Math Fundamentals**

**Focus**: Modular thinking, math tricks

### Easy
1. **Count Primes** (204) - Sieve of Eratosthenes
   - [Problem](https://leetcode.com/problems/count-primes/)
   - Pattern: Math optimization
   - Time: O(n log log n)

2. **Power of Two** (231) - Bit manipulation
   - [Problem](https://leetcode.com/problems/power-of-two/)
   - Pattern: Bit tricks
   - Time: O(1)

3. **Missing Number** (268) - XOR or hash
   - [Problem](https://leetcode.com/problems/missing-number/)
   - Pattern: Bit manipulation or math
   - Time: O(n)

### Medium
1. **Integer Break** (343) - Math optimization
   - [Problem](https://leetcode.com/problems/integer-break/)
   - Pattern: Math
   - Time: O(1)

---

## **Phase 4-5: Data Structures (Arrays, Hashes, Stacks, Queues)**

**Focus**: When to use each DS

### Easy
1. **Best Time to Buy Stock** (121) - Array single pass
   - [Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
   - Pattern: Array tracking
   - Time: O(n), Space: O(1)

2. **Contains Duplicate** (217) - Hash set
   - [Problem](https://leetcode.com/problems/contains-duplicate/)
   - Pattern: Hash set
   - Time: O(n), Space: O(n)

3. **Valid Anagram** (242) - Hash map or sorting
   - [Problem](https://leetcode.com/problems/valid-anagram/)
   - Pattern: Hash map or sorting
   - Time: O(n log n) or O(n)

4. **Majority Element** (169) - Hash map or sorting
   - [Problem](https://leetcode.com/problems/majority-element/)
   - Pattern: Hash map
   - Time: O(n)

5. **Min Stack** (155) - Stack design
   - [Problem](https://leetcode.com/problems/min-stack/)
   - Pattern: Stack with auxiliary storage
   - Time: O(1) per operation

### Medium
1. **LRU Cache** (146) - Hash map + linked list
   - [Problem](https://leetcode.com/problems/lru-cache/)
   - Pattern: Hash map + doubly linked list
   - Time: O(1) per operation

2. **Top K Frequent Elements** (347) - Heap or bucket sort
   - [Problem](https://leetcode.com/problems/top-k-frequent-elements/)
   - Pattern: Heap or bucket sort
   - Time: O(n log k)

---

## **Phase 6: Searching & Sorting**

**Focus**: Binary search, sorting algorithms

### Easy
1. **Binary Search** (704) - Basic binary search
   - [Problem](https://leetcode.com/problems/binary-search/)
   - Pattern: Binary search
   - Time: O(log n)

2. **First Bad Version** (278) - Binary search variant
   - [Problem](https://leetcode.com/problems/first-bad-version/)
   - Pattern: Binary search left boundary
   - Time: O(log n)

### Medium
1. **Search in Rotated Sorted Array** (33) - Modified binary search
   - [Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)
   - Pattern: Binary search with rotation
   - Time: O(log n)

2. **Merge Intervals** (56) - Sorting + merging
   - [Problem](https://leetcode.com/problems/merge-intervals/)
   - Pattern: Sort + iterate
   - Time: O(n log n)

3. **Kth Largest Element** (215) - Heap or quickselect
   - [Problem](https://leetcode.com/problems/kth-largest-element-in-an-array/)
   - Pattern: Heap or quickselect
   - Time: O(n log k) or O(n) avg

---

## **Phase 7: Patterns (Two Pointers, Sliding Window, DP, Backtracking)**

**Focus**: Key interview patterns

### Two Pointers (Easy)
1. **Two Sum II** (167) - Two pointers on sorted
   - [Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
   - Pattern: Two pointers
   - Time: O(n)

2. **Valid Palindrome** (125) - Two pointers with validation
   - [Problem](https://leetcode.com/problems/valid-palindrome/)
   - Pattern: Two pointers
   - Time: O(n)

### Sliding Window (Easy)
1. **Maximum Subarray** (53) - Kadane's algorithm
   - [Problem](https://leetcode.com/problems/maximum-subarray/)
   - Pattern: Sliding window (variant)
   - Time: O(n)

2. **Longest Substring Without Repeating** (3) - Sliding window with hash
   - [Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
   - Pattern: Sliding window
   - Time: O(n)

### Dynamic Programming (Easy)
1. **Climbing Stairs** (70) - Basic DP
   - [Problem](https://leetcode.com/problems/climbing-stairs/)
   - Pattern: 1D DP
   - Time: O(n), Space: O(n) or O(1)

2. **House Robber** (198) - DP tracking
   - [Problem](https://leetcode.com/problems/house-robber/)
   - Pattern: 1D DP
   - Time: O(n)

### Backtracking (Medium)
1. **Permutations** (46) - Full backtracking
   - [Problem](https://leetcode.com/problems/permutations/)
   - Pattern: Backtracking
   - Time: O(n!)

2. **Combinations** (77) - Backtracking with pruning
   - [Problem](https://leetcode.com/problems/combinations/)
   - Pattern: Backtracking
   - Time: O(C(n,k))

---

## **Phase 8-9: Harder Patterns & Practice**

### Two Pointers (Medium)
1. **3Sum** (15) - Two pointers with sorting
   - [Problem](https://leetcode.com/problems/3sum/)
   - Pattern: Two pointers
   - Time: O(n²)

2. **Container With Most Water** (11) - Two pointers optimization
   - [Problem](https://leetcode.com/problems/container-with-most-water/)
   - Pattern: Two pointers
   - Time: O(n)

### Sliding Window (Medium)
1. **Minimum Window Substring** (76) - Complex sliding window
   - [Problem](https://leetcode.com/problems/minimum-window-substring/)
   - Pattern: Sliding window + hash
   - Time: O(n)

2. **Sliding Window Maximum** (239) - Deque optimization
   - [Problem](https://leetcode.com/problems/sliding-window-maximum/)
   - Pattern: Sliding window + deque
   - Time: O(n)

### Dynamic Programming (Medium)
1. **Coin Change** (322) - Unbounded knapsack
   - [Problem](https://leetcode.com/problems/coin-change/)
   - Pattern: 1D DP
   - Time: O(n*m)

2. **Edit Distance** (72) - 2D DP
   - [Problem](https://leetcode.com/problems/edit-distance/)
   - Pattern: 2D DP (Levenshtein)
   - Time: O(m*n)

3. **Longest Increasing Subsequence** (300) - DP + binary search
   - [Problem](https://leetcode.com/problems/longest-increasing-subsequence/)
   - Pattern: DP with binary search optimization
   - Time: O(n log n)

### Backtracking (Medium)
1. **Word Search** (79) - Backtracking + grid
   - [Problem](https://leetcode.com/problems/word-search/)
   - Pattern: DFS backtracking
   - Time: O(n * 4^L)

2. **N-Queens** (51) - Backtracking with constraints
   - [Problem](https://leetcode.com/problems/n-queens/)
   - Pattern: Backtracking
   - Time: O(N!)

---

## **Phase 10: Recursion & Trees**

**Focus**: Tree traversals, recursive thinking

### Easy
1. **Binary Tree Inorder Traversal** (94) - DFS inorder
   - [Problem](https://leetcode.com/problems/binary-tree-inorder-traversal/)
   - Pattern: Tree DFS
   - Time: O(n)

2. **Maximum Depth of Binary Tree** (104) - Tree recursion
   - [Problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
   - Pattern: Tree recursion
   - Time: O(n)

3. **Symmetric Tree** (101) - Tree comparison
   - [Problem](https://leetcode.com/problems/symmetric-tree/)
   - Pattern: Tree recursion
   - Time: O(n)

### Medium
1. **Binary Tree Level Order Traversal** (102) - BFS
   - [Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/)
   - Pattern: Tree BFS
   - Time: O(n)

2. **Path Sum II** (113) - DFS + backtracking
   - [Problem](https://leetcode.com/problems/path-sum-ii/)
   - Pattern: Tree DFS with backtracking
   - Time: O(n)

3. **Lowest Common Ancestor** (236) - Tree LCA
   - [Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
   - Pattern: Tree recursion
   - Time: O(n)

---

## **Phase 11-12: Graphs**

**Focus**: Graph traversals, shortest path, topological sort

### Easy
1. **Number of Islands** (200) - DFS/BFS on grid
   - [Problem](https://leetcode.com/problems/number-of-islands/)
   - Pattern: DFS/BFS on grid
   - Time: O(m*n)

2. **Course Schedule II** (210) - Topological sort
   - [Problem](https://leetcode.com/problems/course-schedule-ii/)
   - Pattern: Topological sort (Kahn's)
   - Time: O(V+E)

### Medium
1. **Clone Graph** (133) - DFS graph copy
   - [Problem](https://leetcode.com/problems/clone-graph/)
   - Pattern: DFS with hash map
   - Time: O(V+E)

2. **Course Schedule** (207) - Cycle detection
   - [Problem](https://leetcode.com/problems/course-schedule/)
   - Pattern: Cycle detection DFS/BFS
   - Time: O(V+E)

3. **Alien Dictionary** (269) - Topological sort
   - [Problem](https://leetcode.com/problems/alien-dictionary/)
   - Pattern: Topological sort + graph building
   - Time: O(N*L + U + E) where N=words, L=len, U=unique chars

### Hard
1. **Network Delay Time** (743) - Dijkstra's algorithm
   - [Problem](https://leetcode.com/problems/network-delay-time/)
   - Pattern: Dijkstra with min-heap
   - Time: O((V+E) log V)

2. **Swim in Rising Water** (778) - Dijkstra on grid
   - [Problem](https://leetcode.com/problems/swim-in-rising-water/)
   - Pattern: Dijkstra on 2D grid
   - Time: O(n² log n)

---

## **Phase 13: Advanced Data Structures**

**Focus**: Union-Find, Segment Tree, Trie

### Union-Find
1. **Number of Connected Components** (323) - Union-Find
   - [Problem](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
   - Pattern: Union-Find
   - Time: O(n * α(n))

2. **Accounts Merge** (721) - Union-Find + hash
   - [Problem](https://leetcode.com/problems/accounts-merge/)
   - Pattern: Union-Find
   - Time: O(n log n)

### Trie
1. **Implement Trie** (208) - Trie data structure
   - [Problem](https://leetcode.com/problems/implement-trie-prefix-tree/)
   - Pattern: Trie implementation
   - Time: O(m) per operation (m=word length)

2. **Word Search II** (212) - Trie + backtracking
   - [Problem](https://leetcode.com/problems/word-search-ii/)
   - Pattern: Trie + DFS
   - Time: O(m*n * 4^L * k) worst case

---

## **Phase 14: Greedy Algorithms**

**Focus**: Activity selection, interval problems

### Medium
1. **Jump Game** (55) - Greedy reach
   - [Problem](https://leetcode.com/problems/jump-game/)
   - Pattern: Greedy
   - Time: O(n)

2. **Jump Game II** (45) - Greedy with tracking
   - [Problem](https://leetcode.com/problems/jump-game-ii/)
   - Pattern: Greedy
   - Time: O(n)

3. **Gas Station** (134) - Greedy choice
   - [Problem](https://leetcode.com/problems/gas-station/)
   - Pattern: Greedy
   - Time: O(n)

4. **Candy** (135) - Greedy two-pass
   - [Problem](https://leetcode.com/problems/candy/)
   - Pattern: Greedy two-pass
   - Time: O(n)

5. **Interval Scheduling** (435) - Activity selection pattern
   - [Problem](https://leetcode.com/problems/non-overlapping-intervals/)
   - Pattern: Greedy sort by end time
   - Time: O(n log n)

### Hard
1. **Video Stitching** (1024) - Greedy interval
   - [Problem](https://leetcode.com/problems/video-stitching/)
   - Pattern: Greedy with intervals
   - Time: O(n)

---

## **Phase 15: String Algorithms**

**Focus**: Pattern matching, substring problems

### Medium
1. **Implement strStr()** (28) - KMP or simple
   - [Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
   - Pattern: String matching
   - Time: O(n+m) with KMP

2. **Longest Palindromic Substring** (5) - Expand around center
   - [Problem](https://leetcode.com/problems/longest-palindromic-substring/)
   - Pattern: String expansion
   - Time: O(n²)

3. **Regular Expression Matching** (10) - DP on strings
   - [Problem](https://leetcode.com/problems/regular-expression-matching/)
   - Pattern: 2D DP
   - Time: O(m*n)

### Hard
1. **Wildcard Matching** (44) - DP with backtracking
   - [Problem](https://leetcode.com/problems/wildcard-matching/)
   - Pattern: 2D DP with greedy
   - Time: O(m*n)

---

## **Phase 16: Advanced Graph**

**Focus**: MST, SCC, bipartite

### Medium
1. **Minimum Spanning Tree (Kruskal)** (1584) - MST construction
   - [Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/)
   - Pattern: Kruskal's MST
   - Time: O(E log E)

2. **Is Graph Bipartite?** (785) - Graph coloring
   - [Problem](https://leetcode.com/problems/is-graph-bipartite/)
   - Pattern: 2-coloring BFS/DFS
   - Time: O(V+E)

### Hard
1. **Critical Connections in Network** (1192) - Find bridges
   - [Problem](https://leetcode.com/problems/critical-connections-in-a-network/)
   - Pattern: Tarjan's algorithm
   - Time: O(V+E)

---

## **Phase 17: Advanced DP**

**Focus**: Complex DP patterns

### Medium
1. **Burst Balloons** (312) - Interval DP
   - [Problem](https://leetcode.com/problems/burst-balloons/)
   - Pattern: Interval DP
   - Time: O(n³)

2. **Shortest Path Visiting All Nodes** (847) - Bitmask DP
   - [Problem](https://leetcode.com/problems/shortest-path-visiting-every-node/)
   - Pattern: Bitmask DP
   - Time: O(2^n * n²)

3. **House Robber III** (337) - Tree DP
   - [Problem](https://leetcode.com/problems/house-robber-iii/)
   - Pattern: Tree DP
   - Time: O(n)

### Hard
1. **Count Digit One** (233) - Digit DP
   - [Problem](https://leetcode.com/problems/digit-sequences-in-increasing-order/)
   - Pattern: Digit DP
   - Time: O(log n)

---

## **Study Strategy**

### By Week (Follow 60-Day Plan)

**Week 1-2**: Do Easy problems from Phases 0-5  
**Week 3-4**: Do Medium problems from Phases 0-5  
**Week 5-6**: Easy + Medium from Phases 6-7  
**Week 7-8**: Medium + Hard from Phases 6-7  
**Week 9-10**: Easy + Medium from Phases 8-10  
**Week 11-12**: Medium + Hard from Phases 11-13  
**Week 13-14**: Medium + Hard from Phases 14-17  

### By Difficulty

**Start**: All Easy problems (build confidence)  
**Progress**: Mix Easy + Medium (70/30)  
**Final**: Medium + Hard (80/20)  

### By Frequency

**High Value** (do first):
- Two Sum variants
- Sliding Window
- DFS/BFS
- Binary Search
- DP basics

---

## **Pro Tips**

1. **Don't just solve** - Understand why each step works
2. **Trace through** - Manually trace at least one example
3. **Optimize** - Always ask "Can this be faster?"
4. **Different approaches** - Solve each problem 2-3 different ways
5. **Timing** - Track how long each problem takes
6. **Review**: Don't solve > 1 new problem/day for first month

---

## **Quick Links**

- [LeetCode](https://leetcode.com)
- [LeetCode Discuss](https://leetcode.com/discuss/)
- [NeetCode 150](https://neetcode.io)
- [Blind 75](https://blindleetcode.com)

---

**Target**: 100+ problems solved by interview time = 95% confidence
