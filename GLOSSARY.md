# 📚 DSA Glossary with Visuals

**50+ terms explained in simple language with diagrams. No jargon.**

---

## 🔤 A - E

### Algorithm
**What:** Step-by-step procedure to solve a problem  
**Example:** Binary search, sorting, BFS  
**Real-world:** Recipe for baking a cake

---

### Array
**What:** Collection of elements stored in sequential memory  
**Visual:**
```
arr = [10, 20, 30, 40, 50]
       0   1   2   3   4   (indices)
```
**Real-world:** Numbered seats in a theater

---

### Big O (O notation)
**What:** How algorithm performance scales with input size  
**Quick reference:**
```
O(1)      - Constant (instant)
O(log n)  - Logarithmic (very fast)
O(n)      - Linear (medium)
O(n²)     - Quadratic (slow)
O(2^n)    - Exponential (very slow)
O(n!)     - Factorial (insanely slow)
```
**Real-world:** How search time grows at library (constant vs linear vs exponential)

---

### Binary Search
**What:** Find element in SORTED array by repeatedly halving search space  
**Visual:**
```
Find 7 in [1, 3, 5, 7, 9, 11]
  Check middle: 5
  7 > 5, search right half
  Check middle: 9
  7 < 9, search left half
  Check middle: 7
  Found!
```
**Complexity:** O(log n)  
**Real-world:** Finding a name in phone book

---

### Binary Tree
**What:** Tree where each node has at most 2 children  
**Visual:**
```
        1
       / \
      2   3
     / \
    4   5
```
**Real-world:** Family tree (each person has up to 2 parents)

---

### Bit Manipulation
**What:** Operations on individual bits (0s and 1s)  
**Common operations:**
```
& (AND):    1 & 1 = 1,  1 & 0 = 0
| (OR):     1 | 0 = 1,  0 | 0 = 0
^ (XOR):    1 ^ 0 = 1,  1 ^ 1 = 0
~ (NOT):    ~1 = 0,     ~0 = 1
```
**Real-world:** Switches in a circuit (on/off states)

---

### BFS (Breadth-First Search)
**What:** Explore graph level by level (all neighbors first)  
**Visual:**
```
Start: 1
Queue: [1]
Visit 1, add neighbors [2, 3]
Queue: [2, 3]
Visit 2, add neighbors [4, 5]
Queue: [3, 4, 5]
```
**Best for:** Shortest path (unweighted graph), finding closest neighbors  
**Real-world:** Spreading a rumor (reaches nearby people first)

---

### Backtracking
**What:** Try all possibilities, undo when stuck  
**Process:**
```
1. Choose candidate
2. Explore with candidate
3. If valid solution found, record it
4. UNDO choice (backtrack)
5. Try next candidate
```
**Best for:** Permutations, combinations, puzzles  
**Real-world:** Trying all combinations on a padlock

---

### Complexity Analysis
**What:** Measuring how algorithm performance scales  
**Two dimensions:**
```
Time: How many operations?
Space: How much memory?

Example: Binary search
Time: O(log n) - halve search space each step
Space: O(1) - only need two pointers
```

---

### Data Structure
**What:** Way of organizing data for efficient operations  
**Common types:**
```
Arrays:   Fast access, slow insertion
Lists:    Flexible, slower than arrays
Stacks:   LIFO (Last In First Out)
Queues:   FIFO (First In First Out)
Trees:    Hierarchical organization
Graphs:   Networks of connections
```

---

### DFS (Depth-First Search)
**What:** Explore graph as deep as possible (go to end of one path first)  
**Visual:**
```
Start: 1
Go deep: 1 -> 2 -> 4 -> 5
Backtrack: 5 (no children)
Backtrack: 4 (no children)
Backtrack: 2 (no children)
Try 3: 1 -> 3
```
**Best for:** Topological sort, finding cycles, connected components  
**Real-world:** Exploring a maze (keep going until dead end, then backtrack)

---

### Dijkstra's Algorithm
**What:** Find shortest path in weighted graph  
**Process:**
```
1. Start at source, distance = 0
2. Mark all others as infinity
3. Visit unvisited node with minimum distance
4. Update neighbors' distances
5. Repeat until destination reached
```
**Complexity:** O((V + E) log V) with priority queue  
**Real-world:** GPS finding shortest driving route

---

## 🔤 E - M

### Dynamic Programming (DP)
**What:** Solve by breaking into subproblems, cache results  
**Key insight:** Optimal solution = combination of optimal subproblems  
**Example:**
```
Fibonacci(5) = Fibonacci(4) + Fibonacci(3)
                    |              |
                    V              V
          Fibonacci(3) + Fib(2)  Fib(2) + Fib(1)
          
Instead of recalculating Fib(3), cache it!
```
**When to use:** Optimization problems, counting problems  
**Real-world:** Planning route (best way to reach each city = best of previous cities + direct)

---

### Edge
**What:** Connection between two nodes in a graph  
**Visual:**
```
Graph with nodes and edges:
  1 --- 2
  |     |
  3 --- 4
  
Edges: (1,2), (1,3), (2,4), (3,4)
```

---

### Greedy Algorithm
**What:** Always pick locally best choice, hope it's globally best  
**Example:**
```
Activity Selection:
Always pick activity that ends earliest
Reason: Leaves room for maximum activities
```
**Danger:** Doesn't work for all problems!  
**When to use:** Problems where greedy choice property proven  
**Real-world:** Coin change (pick largest coin possible)

---

### Hash Map / Hash Table
**What:** Store key-value pairs for O(1) lookup  
**Visual:**
```
{
  "apple": 5,
  "banana": 3,
  "cherry": 7
}

Looking for "banana": instant access in O(1)
```
**Real-world:** Dictionary (look up word instantly)

---

### Heap / Priority Queue
**What:** Data structure where can quickly find minimum (or maximum)  
**Visual:**
```
Min Heap:     Max Heap:
      1             10
     / \           / \
    2   3         8   9
   / \
  4   5
```
**Operations:**
```
Insert: O(log n)
Delete min/max: O(log n)
Find min/max: O(1)
```
**Real-world:** Emergency room (highest priority patient served first)

---

### Heuristic
**What:** Educated guess / rule of thumb for fast solution  
**Example:** A* pathfinding uses heuristic (straight-line distance) to guide search  
**Advantage:** Fast, doesn't guarantee optimal  
**Real-world:** Intuition when solving puzzle (try most promising moves first)

---

### In-place Algorithm
**What:** Algorithm that modifies input without extra space  
**Example:**
```
❌ Not in-place
sorted_arr = sorted(arr)  # Creates new array

✅ In-place
arr.sort()  # Modifies original array
```
**Space complexity:** O(1) for in-place  
**Real-world:** Rearranging books on shelf without extra table

---

### Kruskal's Algorithm (MST)
**What:** Find Minimum Spanning Tree by picking smallest edges  
**Process:**
```
1. Sort all edges by weight
2. For each edge (smallest first):
   - If connects two different components, add it
   - If creates cycle, skip it
3. Continue until n-1 edges added
```
**Complexity:** O(E log E) due to sorting  
**Real-world:** Building roads connecting all cities with minimum cost

---

### Linked List
**What:** Data structure where each element points to next  
**Visual:**
```
[5] -> [10] -> [15] -> [20] -> None

Accessing 15: Must traverse 5 -> 10 -> 15 (O(n))
```
**Advantage:** O(1) insertion/deletion (if have pointer)  
**Disadvantage:** O(n) access  
**Real-world:** Chain (each link points to next link)

---

### Memoization
**What:** Cache results of function calls to avoid recomputation  
**Example:**
```
❌ Without memoization
fib(5):
  fib(4) + fib(3)
  fib(3) + fib(2) + fib(2) + fib(1)  <- fib(3) calculated twice!

✅ With memoization
fib(5):
  fib(4) + fib(3)
  (cached) + (cached)  <- Use cached results!
```
**Real-world:** Remembering phone number so don't look it up twice

---

## 🔤 M - R

### Minimum Spanning Tree (MST)
**What:** Subgraph that connects all nodes with minimum total edge weight  
**Algorithms:** Kruskal, Prim  
**Real-world:** Building network with minimum cable length

---

### Node
**What:** Single element in tree or graph  
**Visual:**
```
      (Node)
       / \
    Node Node
```

---

### Optimization
**What:** Making code faster, using less memory  
**Example:**
```
❌ O(n²) solution
for i in range(n):
  for j in range(n):
    if arr[i] + arr[j] == target:
      return [i, j]

✅ O(n) solution
seen = set()
for num in arr:
  if target - num in seen:
    return [target - num, num]
  seen.add(num)
```

---

### Prim's Algorithm (MST)
**What:** Find Minimum Spanning Tree by growing tree from start node  
**Process:**
```
1. Start with any node
2. Add smallest edge connecting tree to outside node
3. Repeat until all nodes connected
```
**Complexity:** O((V + E) log V) with priority queue  
**Real-world:** Building pipeline from central hub (add closest connection first)

---

### Queue
**What:** FIFO data structure (First In First Out)  
**Visual:**
```
Enqueue: Add to back
[1] -> [2] -> [3] -> back

Dequeue: Remove from front
front <- [1]   [2] -> [3] -> back
```
**Use:** BFS, task scheduling  
**Real-world:** Line at bank (first person served first)

---

### Recursion
**What:** Function calling itself to solve smaller problem  
**Template:**
```
def recursive_function(n):
    if n == 0:  # Base case
        return 0
    return f(n-1) + something  # Recursive case
```
**Warning:** Can be slow, use memoization to speed up  
**Real-world:** Looking up "recursion" in dictionary that says "see recursion"

---

### Recurrence Relation
**What:** Mathematical equation defining recursive relationship  
**Example:**
```
fib(n) = fib(n-1) + fib(n-2)
with fib(0) = 0, fib(1) = 1
```
**Helps:** Analyze recursive algorithm complexity

---

## 🔤 S - Z

### Sliding Window
**What:** Move a "window" across array to find subarrays matching criteria  
**Visual:**
```
Find longest substring without repeating
s = "abcabcbb"

Window at [a]:
Window at [ab]:
Window at [abc]:
Window at [bca]:  <- 'a' repeated, shrink
Window at [cab]:
Window at [cab]:  <- 'b' repeated, shrink
Window at [ab]:
```
**Complexity:** O(n) when done correctly  
**Real-world:** Security camera that records last N seconds

---

### Sorting
**What:** Arranging elements in order  
**Common algorithms:**
```
Merge Sort:    O(n log n) - Always
Quick Sort:    O(n log n) average, O(n²) worst
Heap Sort:     O(n log n) - Always
Insertion:     O(n²) - Slow but simple
```
**Real-world:** Organizing books by author name

---

### Space Complexity
**What:** How much memory algorithm uses  
**Examples:**
```
O(1):  Only use fixed variables
O(n):  Need array of size n
O(n²): Need 2D array of size n×n
```

---

### Stack
**What:** LIFO data structure (Last In First Out)  
**Visual:**
```
Push: Add to top
        [3]
        [2]
top ->  [1]

Pop: Remove from top
[3]
[2]
(removed 1)
```
**Use:** DFS, expression evaluation, undo functionality  
**Real-world:** Stack of plates (grab from top)

---

### String
**What:** Sequence of characters  
**Operations:**
```
"hello"[0] = 'h'      # Access character
"hello"[1:4] = "ell"  # Substring
len("hello") = 5      # Length
"hello" + "world" = "helloworld"  # Concatenation
```
**Caution:** Strings are usually immutable (can't change in place)

---

### Time Complexity
**What:** How many operations algorithm takes  
**Common complexities:**
```
O(1)      - Constant time
O(log n)  - Logarithmic
O(n)      - Linear
O(n log n) - Linearithmic
O(n²)     - Quadratic
O(2^n)    - Exponential
O(n!)     - Factorial
```

---

### Topological Sort
**What:** Order nodes in DAG (Directed Acyclic Graph) such that edges go left to right  
**Example:**
```
Prerequisites:
  A -> B  (A must be done before B)
  B -> C
  A -> C

Valid order: [A, B, C]
```
**Algorithms:** DFS or Kahn's algorithm  
**Real-world:** Course scheduling (take prerequisites first)

---

### Tree
**What:** Acyclic connected graph with hierarchical structure  
**Visual:**
```
        Root
        / \
      /    \
    Node   Node
    / \
   /   \
Leaf   Leaf
```
**Real-world:** Organizational chart, file system

---

### Two Pointers
**What:** Use two indices moving through array (often from opposite ends)  
**Pattern:**
```
left = 0
right = len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```
**Best for:** Sorted arrays, palindromes, pairs  
**Real-world:** Checking if word is palindrome (compare ends moving inward)

---

### Union-Find (Disjoint Set Union)
**What:** Data structure for tracking connected components  
**Operations:**
```
union(a, b):  Connect a and b
find(a):      Find which component a belongs to
```
**Complexity:** Nearly O(1) with path compression  
**Use:** Detecting cycles, MST algorithms  
**Real-world:** Grouping friends (if A friends with B, B with C, then all connected)

---

## 🎯 Quick Reference

| Term | Time | Space | Use |
|------|------|-------|-----|
| Array | O(1) access | O(n) | When need O(1) access |
| Linked List | O(n) access | O(n) | When frequent insertion/deletion |
| Hash Map | O(1) avg | O(n) | When need key-value pairs |
| Heap | O(log n) insert/delete | O(n) | When need min/max repeatedly |
| Stack | O(1) push/pop | O(n) | DFS, expression evaluation |
| Queue | O(1) enqueue/dequeue | O(n) | BFS, task scheduling |
| Binary Search Tree | O(log n) avg | O(n) | Sorted data, search |
| Graph (adjacency list) | O(1) per edge | O(V+E) | Representing networks |

---

**Print this glossary. Reference it while coding. Master these terms.** 💡

