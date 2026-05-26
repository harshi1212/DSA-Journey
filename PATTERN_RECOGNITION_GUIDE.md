# 🎯 Pattern Recognition Guide

**"I have a problem. Which algorithm should I use?"**

This guide answers that question with a flowchart approach. By asking simple questions about the problem, you'll identify the right pattern every time.

---

## 🚀 Quick Decision Tree

```
START: You have a problem
   ↓
Q1: Is it about FINDING something?
   ├─ YES → Q2
   └─ NO → Q8 (Optimization/Construction problems)

Q2: What are you finding?
   ├─ MAXIMUM or MINIMUM? → Q3
   ├─ AN ELEMENT with property X? → Q4
   ├─ ALL elements matching pattern? → Q5
   └─ FIRST/NEXT occurrence? → Q6

Q3: Max/Min problem?
   ├─ Can you make greedy choice? (Local optimum = global) → GREEDY
   ├─ Does optimal = optimal subproblems? → DYNAMIC PROGRAMMING
   ├─ Do items have weight/priority? → PRIORITY QUEUE/HEAP
   └─ On a graph? → DIJKSTRA or BELLMAN-FORD

Q4: Finding an element?
   ├─ Array is sorted? → BINARY SEARCH
   ├─ In a collection? → HASH MAP / HASH SET
   ├─ In a tree/graph? → BFS / DFS / BACKTRACKING
   └─ Specific pattern in array? → TWO POINTERS / SLIDING WINDOW

Q5: Find all matching elements?
   ├─ Generate all combinations? → BACKTRACKING
   ├─ Generate all permutations? → BACKTRACKING
   ├─ Path in tree/graph? → DFS / BACKTRACKING
   ├─ Elements in subarray? → SLIDING WINDOW / HASH MAP
   └─ Unique pairs/triplets? → TWO POINTERS (sorted) or HASH MAP

Q6: Find first occurrence?
   ├─ Sorted array? → BINARY SEARCH
   ├─ Linear search needed? → TWO POINTERS
   ├─ Pattern matching? → KMP / RABIN-KARP / Z-ALGORITHM
   └─ In graph? → BFS (shortest path)

Q8: Optimization/Construction?
   ├─ Build something optimal? → GREEDY or DP
   ├─ Rearrange elements? → SORTING (then two pointers)
   ├─ Minimum spanning tree? → KRUSKAL or PRIM
   ├─ Shortest path? → DIJKSTRA / BFS
   ├─ Strongly connected? → KOSARAJU / TARJAN
   └─ Schedule tasks optimally? → GREEDY

```

---

## 📋 Problem Type → Algorithm Mapping

### By Problem Characteristics

#### "Find the maximum/minimum..."

| Characteristics | Algorithm | Example |
|-----------------|-----------|---------|
| Local choice = global optimal | **Greedy** | Activity Selection, Gas Station |
| Subproblems optimal? | **DP** | Best time to buy stock, Coin change |
| Items have weight/priority | **Heap/Priority Queue** | K largest elements, Meeting rooms |
| Graph-based | **Dijkstra** | Shortest path, Network delay |
| Range queries on array | **Segment Tree** | Range max/min query |

#### "Find the element/index..."

| Characteristics | Algorithm | Example |
|-----------------|-----------|---------|
| Array is sorted | **Binary Search** | Search insert position |
| Need exact match | **Hash Map** | Two Sum, Valid Anagram |
| Contiguous subarray | **Sliding Window** | Longest substring without repeats |
| Distance/gap matters | **Two Pointers** | Container with most water, Trapping rain water |
| Pattern in string | **KMP/Z-algo/Rabin-Karp** | Find all occurrences of pattern |
| In tree/graph | **BFS/DFS** | Path exists, Number of islands |

#### "Find all elements matching..."

| Characteristics | Algorithm | Example |
|-----------------|-----------|---------|
| All combinations | **Backtracking** | Combinations, Power set, Subsets |
| All permutations | **Backtracking** | Permutations, Letter case perms |
| Path in tree/graph | **DFS/Backtracking** | All root to leaf paths, Paths in DAG |
| Subarray property | **Sliding window** | All windows with sum < k |
| Unique pairs/triplets | **Two Pointers** (sorted) | 3Sum, 4Sum |

---

## 🎓 Pattern-by-Pattern Guide

### 1️⃣ TWO POINTERS
**When:** Array problems requiring comparison of two positions
- Sorted arrays
- Finding pairs/triplets
- Palindromes
- Container problems

**Red flags (problems likely TWO POINTERS):**
- "Two integers in array that sum to X"
- "Trapping water/container"
- "Remove duplicates"
- "Reverse in place"
- "Palindrome check"

**Example:**
```python
# Find pair that sums to target
left, right = 0, n-1
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1
```

---

### 2️⃣ SLIDING WINDOW
**When:** Subarray/substring problems with constraints
- Longest/shortest subarray with property
- Count of subarrays matching constraint
- All windows with specific property

**Red flags:**
- "Longest substring with..."
- "Maximum sum subarray with..."
- "All subarrays where..."
- Uses max window size

**Example:**
```python
# Longest substring without repeating
left = 0
char_map = {}
max_len = 0

for right in range(len(s)):
    if s[right] in char_map:
        left = max(left, char_map[s[right]] + 1)
    char_map[s[right]] = right
    max_len = max(max_len, right - left + 1)
```

---

### 3️⃣ BINARY SEARCH
**When:** Sorted data + seeking element or making decision
- Exact match in sorted array
- First/last occurrence
- Closest element
- Feasibility check (minimizing/maximizing)

**Red flags:**
- "Sorted array"
- "Rotated sorted array"
- "Find first position where..."
- "Minimize/maximize... (with decision function)"

**Example:**
```python
# Find first position >= target
left, right = 0, len(nums)
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left
```

---

### 4️⃣ DYNAMIC PROGRAMMING
**When:** Optimal substructure + overlapping subproblems
- Max/min path to goal
- Counting ways to achieve goal
- Sequence optimization

**Red flags:**
- "Ways to...", "Number of ways..."
- "Maximum/minimum path..."
- "Can you achieve..."
- Optimal = combining optimal subproblems

**Example:**
```python
# Coin change - minimum coins
dp = [inf] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
```

---

### 5️⃣ BACKTRACKING
**When:** Generate all possibilities with constraints
- All permutations/combinations
- All valid expressions
- All paths

**Red flags:**
- "All...", "Generate all...", "List all..."
- "Permutation", "Combination"
- Path problems
- NP-complete problems (small input size)

**Example:**
```python
# Combinations
def backtrack(start, combo):
    if len(combo) == k:
        result.append(combo[:])
        return
    for i in range(start, n + 1):
        combo.append(i)
        backtrack(i + 1, combo)
        combo.pop()
```

---

### 6️⃣ BFS / DFS
**When:** Graph/tree traversal or shortest path (unweighted)
- Connected components
- Level order traversal
- Shortest path (unweighted)
- Tree problems

**Red flags:**
- "Tree", "Graph"
- "Connected components", "Islands"
- "Shortest path (in unweighted graph)"
- "Level order", "Depth first"

**Example:**
```python
# BFS - shortest path
from collections import deque
queue = deque([start])
dist = {start: 0}

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if v not in dist:
            dist[v] = dist[u] + 1
            queue.append(v)
```

---

### 7️⃣ GREEDY
**When:** Local optimal choice = global optimal (prove before coding!)
- Activity selection
- Interval problems
- Huffman coding
- Classic greedy problems

**Red flags:**
- "Maximum activities", "Maximum meetings"
- "Minimum meetings rooms"
- "Gas station", "Jump game"
- Always pick locally best option

**Important:** Greedy doesn't always work! Must prove greedy choice property.

**Example:**
```python
# Activity selection
activities.sort(key=lambda x: x[1])
selected = [activities[0]]
for i in range(1, len(activities)):
    if activities[i][0] >= selected[-1][1]:
        selected.append(activities[i])
```

---

### 8️⃣ SORTING
**When:** Preprocessing + reordering
- Before two pointers
- Before binary search
- Group similar elements

**Red flags:**
- "Sort the array"
- "Before two pointer approach"
- "K largest/smallest"
- "Group elements"

---

## 🎯 Decision Framework

### Step 1: Understand the Problem
- [ ] What are we finding/optimizing?
- [ ] What constraints exist?
- [ ] What's the input/output format?

### Step 2: Check Data Structure
- [ ] Array? → Sorting, two pointers, sliding window, binary search
- [ ] Tree? → DFS, BFS, recursion
- [ ] Graph? → BFS, DFS, Dijkstra, topological sort
- [ ] String? → Sliding window, pattern matching, DP
- [ ] Need counting? → Hash map/set

### Step 3: Check Problem Type
- [ ] Finding? → Linear search, binary search, hash map
- [ ] Optimizing? → Greedy or DP
- [ ] Generating? → Backtracking
- [ ] Traversing? → BFS/DFS
- [ ] Sorting? → Merge sort, quick sort, heap sort

### Step 4: Check Constraints
- [ ] Small n (≤ 20)? → Backtracking is OK
- [ ] Need all combinations? → Backtracking/DP
- [ ] Need sorted array? → Sort first (O(n log n))
- [ ] Sorted already? → Binary search (O(log n))
- [ ] Can't modify input? → Extra space needed

---

## 📚 Pattern Complexity Cheat Sheet

| Pattern | Best Case | Average | Worst | Space | Use When |
|---------|-----------|---------|-------|-------|----------|
| **Two Pointers** | O(n) | O(n) | O(n) | O(1) | Sorted array, pairs |
| **Sliding Window** | O(n) | O(n) | O(n) | O(k) | Subarray constraints |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) | Sorted, decision |
| **DP** | O(n) | O(n-n²) | O(n²-n³) | O(n) | Subproblems |
| **Backtracking** | O(n!) | O(n!) | O(n!) | O(n) | All combinations |
| **BFS/DFS** | O(V+E) | O(V+E) | O(V+E) | O(V) | Graph traversal |
| **Greedy** | O(1) | O(n log n) | O(n log n) | O(1) | Activity selection |
| **Binary Search + Modification** | O(n log n) | O(n log n) | O(n log n) | O(1) | Optimization |

---

## 🔥 Problem Classification Exercise

**Try these:**

1. **"Find two numbers that sum to target"**
   - Answer: Two Pointers (sort first if needed)
   
2. **"Maximum length substring without repeating characters"**
   - Answer: Sliding Window + Hash Map
   
3. **"Find peak element in rotated sorted array"**
   - Answer: Binary Search (modified)
   
4. **"Number of ways to climb stairs"**
   - Answer: Dynamic Programming
   
5. **"Generate all permutations of array"**
   - Answer: Backtracking
   
6. **"Connected components in undirected graph"**
   - Answer: DFS or Union-Find
   
7. **"Activity selection problem"**
   - Answer: Greedy (sort by end time)
   
8. **"Minimum cost to connect all cities"**
   - Answer: Minimum Spanning Tree (Kruskal/Prim)

---

## 💡 Pro Tips

### Tip 1: When Confused
- List characteristics of the problem
- Match against this guide
- Start coding the matching pattern

### Tip 2: Multiple Patterns Fit?
- Prefer simpler solution first
- If too slow, optimize with advanced pattern
- Example: Brute force → Two pointers → Binary search

### Tip 3: Interview Approach
1. "This looks like a **[pattern]** problem"
2. "Here's why: [explain characteristics]"
3. "Let me code a solution..."
4. "Complexity: O(time) and O(space)"

### Tip 4: Pattern Combinations
Many hard problems combine patterns:
- Sort + Two pointers = O(n log n) for two-pointer problem
- Hash map + Sliding window = efficient substring problems
- BFS + DP = shortest path to collect items
- Greedy + DP = optimal scheduling

---

## 🎓 Learning Path

By phase, you'll master:
- Phase 0-1: Basics
- Phase 2-5: Data structures (prepare for patterns)
- **Phase 7**: Two pointers, sliding window, DP, backtracking
- **Phase 9**: Practice (apply pattern recognition)
- **Phase 12-13**: Graphs (BFS, DFS, advanced patterns)
- **Phase 14-17**: Greedy, strings, advanced topics (combining patterns)

---

## 📖 Quick Reference Card

**Save this decision tree:**

```
"Which pattern?"

├─ Sorted array? → Binary Search
├─ Subarray constraint? → Sliding Window
├─ Two positions related? → Two Pointers
├─ Max/min with subproblems? → DP
├─ Generate all? → Backtracking
├─ Tree/Graph traversal? → BFS/DFS
├─ Local optimal = global? → Greedy
├─ Unsorted, need structure? → Sort + Pattern
└─ Multiple criteria? → Combine patterns!
```

---

**Master this guide. Solve any DSA problem.** 💪

