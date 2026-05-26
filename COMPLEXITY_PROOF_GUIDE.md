# 📐 Complexity Proof Guide

**Understand WHY algorithms have their stated complexity. Prove Big O claims mathematically.**

---

## Part 1: Big O Definition & Proof Notation

### What "O(f(n))" Really Means

**Definition:** $O(f(n))$ means there exist constants $c > 0$ and $n_0$ such that:
$$T(n) \leq c \cdot f(n) \text{ for all } n \geq n_0$$

**In plain English:** Eventually (after some point), the algorithm's actual operations are bounded by $c \times f(n)$.

---

### Example Proof: Linear Search is O(n)

**Algorithm:**
```python
def linear_search(arr, target):
    for i in range(len(arr)):        # Line A
        if arr[i] == target:         # Line B
            return i
    return -1
```

**Operation Count:**
- Worst case: target not found
- Loop runs exactly $n$ times (where $n = len(arr)$)
- Each iteration: Line A (1 op) + Line B (1 op) = 2 ops
- Total operations: $T(n) = 2n$

**Proof that $T(n) = O(n)$:**
- We need to show: $2n \leq c \cdot n$ for some $c$
- Choose $c = 3$: Then $2n \leq 3 \cdot n$ ✅ (always true for $n \geq 1$)
- Therefore: Linear Search is $O(n)$

---

### Example Proof: Binary Search is O(log n)

**Algorithm:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Operation Count:**
- Each iteration: 3-4 operations (constant)
- Key insight: Search space halves each iteration

| Iteration | Search Space Size |
|-----------|------------------|
| 0         | n                |
| 1         | n/2              |
| 2         | n/4              |
| 3         | n/8              |
| k         | n/2^k            |

- Algorithm stops when search space = 1: $n/2^k = 1$
- Solve for k: $2^k = n \Rightarrow k = \log_2(n)$
- So loop runs at most $\log_2(n) + 1$ times
- Operations per iteration: constant (4)
- Total: $T(n) = 4(\log_2(n) + 1) = 4\log_2(n) + 4$

**Proof that $T(n) = O(\log n)$:**
- We need: $4\log_2(n) + 4 \leq c \cdot \log_2(n)$
- Choose $c = 5$ and $n_0 = 2$
- Check: $4\log_2(2) + 4 = 4(1) + 4 = 8$, and $5 \cdot \log_2(2) = 5(1) = 5$... doesn't work
- Try larger $c$: choose $c = 8$
- For $n = 16$: $4\log_2(16) + 4 = 4(4) + 4 = 20$, and $8 \cdot \log_2(16) = 8(4) = 32$ ✅
- Therefore: Binary Search is $O(\log n)$

---

## Part 2: Recurrence Relations & Master Theorem

### What's a Recurrence Relation?

**Definition:** Equation defining a function in terms of itself

**Example: Merge Sort**
```
T(n) = 2·T(n/2) + n
       └─ recursive calls
           └─ sorting left and right halves
           └─ merging takes O(n) time
```

**Meaning:**
- To sort $n$ elements:
  - Recursively sort $n/2$ elements (left half): $T(n/2)$
  - Recursively sort $n/2$ elements (right half): $T(n/2)$
  - Merge them: $O(n) = n$ operations
- Total: $T(n) = 2 \cdot T(n/2) + n$

---

### Master Theorem (The Shortcut)

**For recurrences of form:** $T(n) = a \cdot T(n/b) + f(n)$

Where:
- $a$ = number of recursive calls
- $b$ = factor by which problem shrinks
- $f(n)$ = cost of non-recursive work

**Cases:**

| Case | Condition | Result |
|------|-----------|--------|
| 1 | $f(n) = O(n^{d})$ where $d < \log_b(a)$ | $T(n) = O(n^{\log_b(a)})$ |
| 2 | $f(n) = O(n^{d} \log^k n)$ where $d = \log_b(a)$ | $T(n) = O(n^d \log^{k+1} n)$ |
| 3 | $f(n) = O(n^{d})$ where $d > \log_b(a)$ | $T(n) = O(f(n))$ |

---

### Applying Master Theorem: Merge Sort

**Recurrence:** $T(n) = 2 \cdot T(n/2) + n$

**Identify:**
- $a = 2$ (2 recursive calls)
- $b = 2$ (halving problem size)
- $f(n) = n$ (merging cost)
- $d = 1$ (since $f(n) = n = n^1$)

**Check which case:**
- $\log_b(a) = \log_2(2) = 1$
- $d = 1$, so $d = \log_b(a)$ ✓ **Case 2**

**Apply Case 2 (with $k=0$):**
$$T(n) = O(n^1 \log^{0+1} n) = O(n \log n)$$

**Therefore: Merge Sort is $O(n \log n)$** ✅

---

### Applying Master Theorem: Fibonacci

**Recurrence:** $T(n) = T(n-1) + T(n-2) + 1$

**Problem:** Doesn't fit Master Theorem form!

**Why?** Master Theorem requires $T(n/b)$ (dividing), not $T(n-1), T(n-2)$ (subtracting).

**Instead, use iteration:**
- $T(n) = T(n-1) + T(n-2) + 1$
- Unroll: $T(n-1) = T(n-2) + T(n-3) + 1$
- Notice: Each level has exponentially more work
- Total nodes at level $k$ ≈ $2^k$
- Tree has $n$ levels
- Total operations ≈ $1 + 2 + 4 + 8 + ... + 2^n = 2^{n+1} - 1$

**Therefore: Naive Fibonacci is $O(2^n)$** ❌ (Very slow!)

---

### Fibonacci with Memoization

**Recurrence:** $T(n) = 2 \cdot T(n-2) + 1$, but each subproblem computed once

**Key insight:** Memoization means each $T(k)$ for $k < n$ calculated exactly once

**Operation count:**
- $n$ unique subproblems: $T(0), T(1), T(2), ..., T(n)$
- Each takes $O(1)$ time (lookup or calculation)
- Total: $O(n)$

**Therefore: Fibonacci with DP is $O(n)$** ✅ (Much better!)

---

## Part 3: Common Algorithm Proofs

### Proof 1: Bubble Sort is $O(n^2)$

**Algorithm:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Outer loop: n times
        for j in range(n-i-1):   # Inner loop: n-1, n-2, ..., 1 times
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])
```

**Operation count:**
- Outer loop: $n$ iterations
- Inner loop iteration $i$: $(n - i - 1)$ comparisons
- Total comparisons:
$$\sum_{i=0}^{n-1} (n-i-1) = (n-1) + (n-2) + ... + 1 + 0 = \frac{n(n-1)}{2}$$

**Simplify:**
$$T(n) = \frac{n(n-1)}{2} = \frac{n^2 - n}{2}$$

**Proof that $T(n) = O(n^2)$:**
- We need: $\frac{n^2 - n}{2} \leq c \cdot n^2$
- Divide by $n^2$: $\frac{1}{2} - \frac{1}{n} \leq c$
- For large $n$, this approaches $\frac{1}{2}$
- Choose $c = 1$: ✅ True for all $n \geq 1$

**Therefore: Bubble Sort is $O(n^2)$** ✅

---

### Proof 2: Binary Search Tree Search is $O(\log n)$ Average

**Setup:**
- Balanced BST with $n$ nodes
- Searching for target

**Analysis:**
- Start at root (1 comparison)
- If target is at root: done (1 operation)
- If target < root: search left subtree
- If target > root: search right subtree

**Key insight:** Balanced BST has height $h = \log_2(n)$

**Worst case:** Target is leaf at bottom
- Must traverse from root to leaf
- Operations: $h = \log_2(n)$ comparisons
- Total: $T(n) = O(\log n)$

**Unbalanced BST:** If tree becomes linear (all nodes in chain):
- Height $h = n$
- Operations: $n$ comparisons
- Total: $T(n) = O(n)$ ❌

**Therefore: Balanced BST search is $O(\log n)$, unbalanced is $O(n)$** ⚖️

---

### Proof 3: Quick Sort is $O(n \log n)$ Average

**Algorithm:**
```
QuickSort(arr, low, high):
    if low < high:
        p = Partition(arr, low, high)     # O(n) - linear pass
        QuickSort(arr, low, p-1)          # T(p-1)
        QuickSort(arr, p+1, high)         # T(n-p)
```

**Average case:** Partition is roughly balanced (splits into $n/2$ and $n/2$)

**Recurrence:** $T(n) = 2 \cdot T(n/2) + n$

**This is identical to Merge Sort!** Apply Master Theorem:
- $a = 2$, $b = 2$, $f(n) = n$, $d = 1$
- $\log_b(a) = 1 = d$ → Case 2
- $T(n) = O(n \log n)$

**Worst case:** Partition is unbalanced (splits into $0$ and $n-1$)

**Recurrence:** $T(n) = T(n-1) + n$

**Solve by iteration:**
$$T(n) = n + (n-1) + (n-2) + ... + 1 = \frac{n(n+1)}{2} = O(n^2)$$

**Therefore: Quick Sort is $O(n \log n)$ average, $O(n^2)$ worst case** 📊

---

### Proof 4: BFS/DFS is $O(V + E)$

**Setup:**
- Graph with $V$ vertices and $E$ edges
- Visit each vertex once, check each edge

**Algorithm:**
```
BFS/DFS(graph):
    visited = set()
    for each vertex v:                    # O(V)
        if v not visited:
            queue.append(v)
            while queue not empty:
                node = queue.pop()
                mark visited
                for each neighbor of node:  # Total: O(E)
                    if neighbor not visited:
                        queue.append(neighbor)
```

**Operation count:**
- Visiting each of $V$ vertices: $O(V)$
- Checking each of $E$ edges: $O(E)$
  - Each edge explored once from each endpoint
  - Total: $O(E)$
- Total: $T(n) = O(V + E)$

**Example:** Tree with 5 nodes (4 edges)
- Visit nodes: 5 operations
- Check edges: 4 operations
- Total: 9 ✅

**Therefore: BFS/DFS is $O(V + E)$** ✅

---

### Proof 5: Merge Operation is $O(n)$

**Algorithm:**
```python
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):   # While both have elements
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])   # Add remaining
    result.extend(right[j:])
    return result
```

**Operation count:**
- Main loop: While loop runs until all elements from one array exhausted
  - Left loop iterations: $|\text{left}|$
  - Right loop iterations: $|\text{right}|$
  - Total iterations: $|\text{left}| + |\text{right}| = n$
- Adding remaining: $O(n)$ to copy rest
- Total: $T(n) = 2n = O(n)$

**Therefore: Merge operation is $O(n)$** ✅

---

## Part 4: Space Complexity Proofs

### Proof: Recursion Stack Space

**Problem:** What's space complexity of recursive function?

**Example: Fibonacci**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**Analysis:**
- Each call adds frame to call stack
- Deepest call stack: $fib(n) → fib(n-1) → fib(n-2) → ... → fib(1) → fib(0)$
- Maximum depth: $n$ frames
- Each frame uses $O(1)$ space
- Total stack space: $O(n)$

**Therefore: Naive Fibonacci recursive space is $O(n)$** 📚

### Proof: Hash Map Space

**Problem:** Space complexity of storing n elements in hash map?

**Analysis:**
- Hash map stores $n$ key-value pairs
- Each pair uses constant space
- Total: $O(n)$ space

**Note:** Load factor affects internal hash table size, but still $O(n)$

**Therefore: Hash map space for $n$ elements is $O(n)$** 📚

---

## Part 5: Practice Problems with Proofs

### Problem 1: Sum of Array (Prove $O(n)$ time)

```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

**Proof:**
- Loop runs exactly $n$ times (where $n = \text{len}(arr)$)
- Each iteration: constant operations (add, assignment)
- Total: $T(n) = c \cdot n$ where $c$ is constant
- Therefore: $T(n) = O(n)$ ✅

---

### Problem 2: Nested Loops (Prove $O(n^2)$ time)

```python
def find_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
```

**Proof:**
- Outer loop: $n$ iterations
- Inner loop: $n$ iterations per outer loop iteration
- Total iterations: $n \times n = n^2$
- Each iteration: constant operations
- Total: $T(n) = c \cdot n^2$
- Therefore: $T(n) = O(n^2)$ ✅

---

### Problem 3: Nested Loops with Break (Prove $O(n^2)$ time)

```python
def search_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == target:
                return (i, j)
```

**Proof:**
- Worst case: target not found or at end
- Outer loop: $n$ iterations
- Inner loop: $n$ iterations
- Best case: $O(1)$ (target at start)
- Worst case: $O(n^2)$ (target not found)
- Average case: $O(n^2/2)$ (on average, check half)
- Asymptotic: $O(n^2)$ ✅

---

## Reference: Big O Hierarchy

From fastest to slowest:

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$

```
Constant           O(1)      ✅ Instant
Logarithmic        O(log n)  ✅ Very fast
Linear             O(n)      ✅ Fast
Linearithmic       O(n log n) ✅ Good
Quadratic          O(n²)     ⚠️  Slow for large n
Cubic              O(n³)     ❌ Very slow
Exponential        O(2^n)    🔥 Impossibly slow
Factorial          O(n!)     💀 Don't even try
```

---

**Master these proofs. Understand your algorithms deeply. Explain complexity with confidence.** 📐

