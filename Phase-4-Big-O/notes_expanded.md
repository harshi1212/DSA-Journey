# Phase 4 - Big O Notation & Complexity Analysis (Master Edition)

**The single most important concept for DSA interviews. Master this completely.**

---

## Table of Contents
1. [Formal Definitions](#formal-definitions)
2. [Mathematical Foundations](#mathematical-foundations)
3. [Big O Notation Deep Dive](#big-o-notation-deep-dive)
4. [Analyzing Code Complexity](#analyzing-code-complexity)
5. [Common Complexities](#common-complexities)
6. [Space Complexity](#space-complexity)
7. [Comparing Algorithms](#comparing-algorithms)
8. [Worked Examples (50+)](#worked-examples)
9. [Complexity Proofs](#complexity-proofs)
10. [Practice Problems](#practice-problems)
11. [Interview Preparation](#interview-preparation)

---

# FORMAL DEFINITIONS

## What is Big O Notation?

**Definition (Mathematical):**
Big O notation describes the upper bound on the time or space complexity of an algorithm.

Let $f(n)$ and $g(n)$ be functions from positive integers to positive reals.

We write $f(n) = O(g(n))$ if there exist positive constants $c$ and $n_0$ such that:

$$f(n) \leq c \cdot g(n) \text{ for all } n \geq n_0$$

**In Plain English:** "Eventually (after some point), the algorithm's operations are bounded by a constant times g(n)."

---

## Why Big O Matters

**Real-world impact:**
```
Problem: Sort 1 million numbers

Algorithm A: O(n²)
Operations: 1,000,000² = 10^12
Time: ~11 days on modern computer

Algorithm B: O(n log n)
Operations: 1,000,000 × log₂(1,000,000) ≈ 20,000,000
Time: ~0.02 seconds on modern computer

Difference: 10^6 times faster! ← This is why Big O matters
```

---

## Notation Variants

| Notation | Name | Meaning | Example |
|----------|------|---------|---------|
| **O(g(n))** | Big O | Upper bound | Worst case |
| **Ω(g(n))** | Big Omega | Lower bound | Best case |
| **Θ(g(n))** | Big Theta | Tight bound | Average case |
| **o(g(n))** | Little o | Strictly less | |
| **ω(g(n))** | Little omega | Strictly greater | |

---

# MATHEMATICAL FOUNDATIONS

## Growth Rates Hierarchy

From fastest to slowest:

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$

**Visualization - Operations count as n grows:**

```
n = 1000

O(1):           1 operation
O(log n):       ~10 operations (log₂ 1000)
O(n):           1,000 operations
O(n log n):     ~10,000 operations
O(n²):          1,000,000 operations
O(n³):          1,000,000,000 operations
O(2^n):         10^301 operations (IMPOSSIBLE!)
O(n!):          Infinite (practically)
```

---

## Asymptotic Analysis (Why We Ignore Constants)

**Problem:** Compare these algorithms
```
Algorithm A: T(n) = 100n + 50
Algorithm B: T(n) = 2n + 1000
Algorithm C: T(n) = n²
```

**When n = 10:**
- A: 100(10) + 50 = 1,050
- B: 2(10) + 1,000 = 1,020
- C: 10² = 100

**When n = 1,000:**
- A: 100(1,000) + 50 = 100,050
- B: 2(1,000) + 1,000 = 3,000
- C: 1,000² = 1,000,000

**When n = 1,000,000:**
- A: 100(1,000,000) + 50 = 100,000,050
- B: 2(1,000,000) + 1,000 = 2,001,000
- C: 1,000,000² = 1,000,000,000,000

**Insight:** For large n, only the highest-order term matters!
- A and B are both O(n) (B becomes faster due to better constant)
- C is O(n²) (grows much faster)
- For very large n, C is thousands of times slower than A and B

---

## Mathematical Proofs

### Proving 2n² + 3n + 1 is O(n²)

We need to prove: $\exists c > 0, n_0 > 0$ such that $2n^2 + 3n + 1 \leq c \cdot n^2$ for all $n \geq n_0$

**Proof:**
$$2n^2 + 3n + 1 \leq 2n^2 + 3n^2 + n^2 = 6n^2$$

(valid for $n \geq 1$)

So choose $c = 6$ and $n_0 = 1$:
$$2n^2 + 3n + 1 \leq 6 \cdot n^2 \text{ for all } n \geq 1 \quad \checkmark$$

Therefore: $2n^2 + 3n + 1 = O(n^2)$

### Why is 2n NOT O(n)?

We want to prove: There exist $c > 0, n_0 > 0$ such that $2n \leq c \cdot n$ for all $n \geq n_0$

**Proof:**
Choose ANY $c > 0$. Then $2n \leq c \cdot n$ requires $2 \leq c$.

If $c \geq 2$, then the inequality holds for ALL $n \geq n_0$ (including $n_0 = 1$).

So $n_0 = 1, c = 2$ works. Therefore: $2n = O(n)$

---

# BIG O NOTATION DEEP DIVE

## O(1) - Constant Time

**Definition:** Algorithm takes the same time regardless of input size

**Characteristics:**
- No loops
- No recursion (without branching)
- Direct computation
- Time doesn't depend on n

**Examples:**
```python
# O(1): Getting first element
first = arr[0]

# O(1): Dictionary lookup (average case)
value = dictionary["key"]

# O(1): Checking if list is empty
is_empty = len(lst) == 0

# O(1): Arithmetic operation
result = 5 + 3

# O(1): Stack operations
stack.push(value)
stack.pop()
```

**Visual - As input grows:**
```
Time
  |
  |●
  |●
  |●
  |●●●●●●●●●●●●●●●●●●●●●
  |___________________________ Input size
  
All operations take same time
```

---

## O(n) - Linear Time

**Definition:** Algorithm's time grows proportionally with input size

**Characteristics:**
- Single loop through n items
- Processing each item once
- Time doubles when input doubles

**Examples:**
```python
# O(n): Finding maximum element
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num

# O(n): Sum all elements
total = 0
for num in arr:
    total += num

# O(n): Linear search
for num in arr:
    if num == target:
        return True

# O(n): Creating new list
new_list = [x * 2 for x in arr]
```

**Analysis - Operations count:**
```
Input size n = 5: ~5 operations
Input size n = 10: ~10 operations
Input size n = 100: ~100 operations
Input size n = 1,000: ~1,000 operations

Pattern: operations ≈ n
Therefore: O(n)
```

---

## O(n²) - Quadratic Time

**Definition:** Algorithm's time grows with square of input size

**Characteristics:**
- Nested loops
- Each loop runs n times
- Operations = n × n = n²

**Examples:**
```python
# O(n²): Bubble sort
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            swap(arr[j], arr[j+1])

# O(n²): Checking all pairs
for i in range(n):
    for j in range(n):
        print(arr[i], arr[j])

# O(n²): Naive search for duplicates
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            return True
```

**Analysis - Operations count:**
```
Input size n = 5: 25 operations
Input size n = 10: 100 operations
Input size n = 100: 10,000 operations
Input size n = 1,000: 1,000,000 operations

Pattern: operations ≈ n²
When n doubles, operations quadruple!
```

---

## O(log n) - Logarithmic Time

**Definition:** Algorithm eliminates half of input each iteration

**Characteristics:**
- Each step reduces problem size by factor
- Usually a "divide and conquer" approach
- log₂(1,000,000) ≈ 20 steps only!

**Examples:**
```python
# O(log n): Binary search
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# O(log n): Integer division until 1
n = 100
while n > 1:
    n = n // 2  # Halves each time
```

**Analysis - Why log n?**
```
n = 1: Need 0 divisions
n = 2: Need 1 division
n = 4: Need 2 divisions
n = 8: Need 3 divisions
n = 16: Need 4 divisions
n = 1,000,000: Need ~20 divisions!

Pattern: Each step halves n
Operations = log₂(n)
```

---

## O(n log n) - Linearithmic Time

**Definition:** Combination of linear and logarithmic

**Characteristics:**
- Often from "divide and conquer" sorting
- More efficient than O(n²) but slower than O(n)
- Most sorting algorithms are O(n log n)

**Examples:**
```python
# O(n log n): Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # O(log n) depth
    right = merge_sort(arr[mid:])
    return merge(left, right)         # O(n) merge

# O(n log n): Sorting algorithm
sorted_arr = sorted(arr)  # Python uses Timsort (O(n log n))

# O(n log n): Building BST with sorted insertion
for num in arr:
    bst.insert(num)  # O(log n) per insertion × n insertions
```

**Analysis - Why n log n?**
```
Merge sort example with n = 8:
Level 0: Split        [1,3,5,7,2,4,6,8]      (1 level, n ops)
Level 1: Split pairs  [1,3] [5,7] [2,4] [6,8] (2 levels, n ops each)
Level 2: Split        [1] [3] [5] [7] ...     (3 levels, n ops each)

Total: n + n + n = 3n = 8 × log₂(8) = 8 × 3 = 24 operations
Operations = n × log₂(n)
```

---

## O(2^n) - Exponential Time

**Definition:** Algorithm's time doubles with each additional input

**Characteristics:**
- AVOID! Practically impossible for large n
- Usually recursive without pruning
- Only feasible for n ≤ 20

**Examples:**
```python
# O(2^n): Naive Fibonacci (SLOW!)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
    # Each call makes 2 more calls = 2^n total calls

# O(2^n): All subsets of a set
def all_subsets(arr):
    result = []
    for i in range(2**len(arr)):  # 2^n possible subsets
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    return result

# O(2^n): Brute force password search
for i in range(2**password_length):
    try_password(i)
```

**Analysis - Why so slow?**
```
n = 10: 2^10 = 1,024 operations
n = 20: 2^20 = 1,000,000 operations
n = 30: 2^30 = 1,000,000,000 operations (1 second)
n = 40: 2^40 = 1,000,000,000,000 operations (1 hour+)
n = 50: 2^50 = ... (days)

Each additional item DOUBLES total operations!
```

---

## O(n!) - Factorial Time

**Definition:** Algorithm tries all permutations

**Characteristics:**
- Even worse than exponential!
- Only feasible for n ≤ 10
- Generate all permutations/combinations without optimization

**Examples:**
```python
# O(n!): Generate all permutations
from itertools import permutations
for perm in permutations(arr):  # n! permutations
    process(perm)

# O(n!): Traveling salesman problem (brute force)
def tsp_brute_force(cities):
    best_route = None
    for route in permutations(cities):  # n! routes
        if distance(route) < distance(best_route):
            best_route = route
    return best_route
```

**Analysis - How bad?**
```
n = 5: 5! = 120
n = 10: 10! = 3,628,800
n = 12: 12! = 479,001,600
n = 13: 13! = 6,227,020,800

Practically impossible beyond n = 13
```

---

# ANALYZING CODE COMPLEXITY

## Step-by-Step Analysis Method

**Process:**
1. Identify loops and recursion
2. Count operations in each block
3. Multiply for nested blocks
4. Keep only highest-order term
5. Drop constants

### Example 1: Simple Loop
```python
def example1(arr):
    total = 0        # O(1)
    for num in arr:  # Loop n times
        total += num # O(1) inside loop
    return total     # O(1)

# Analysis:
# Line 1: O(1)
# Line 2-3: O(n) [n iterations, each O(1)]
# Line 4: O(1)
# Total: O(1) + O(n) + O(1) = O(n)
```

### Example 2: Nested Loops
```python
def example2(arr):
    for i in range(len(arr)):      # n iterations
        for j in range(len(arr)):  # n iterations per i
            print(arr[i][j])       # O(1)

# Analysis:
# Outer loop: n times
# Inner loop: n times per outer iteration
# Body: O(1)
# Total: n × n × O(1) = O(n²)
```

### Example 3: Nested Loops with Different Ranges
```python
def example3(arr):
    for i in range(len(arr)):           # n iterations
        for j in range(len(arr) - i):   # (n-i) iterations per i
            print(arr[i] + arr[j])      # O(1)

# Analysis:
# Iteration i=0: n operations
# Iteration i=1: n-1 operations
# Iteration i=2: n-2 operations
# ...
# Total: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n²)

# Rule: Even if inner loop count varies, total is still O(n²)
```

### Example 4: Sequential Operations
```python
def example4(arr):
    # Block 1
    for i in range(len(arr)):    # O(n)
        print(arr[i])
    
    # Block 2
    for i in range(len(arr)):    # O(n)
        for j in range(len(arr)): # O(n²)
            print(arr[i][j])

# Analysis:
# Block 1: O(n)
# Block 2: O(n²)
# Total: O(n) + O(n²) = O(n²)

# Rule: Take the MAXIMUM complexity
# (Higher complexity dominates)
```

### Example 5: Conditional with Branch
```python
def example5(arr, target):
    if len(arr) == 0:              # O(1)
        return -1
    
    for num in arr:                # O(n)
        if num == target:
            return num              # O(1)
    
    return -1

# Analysis:
# Best case: target at position 0 = O(1)
# Worst case: target not found = O(n)
# Average case: O(n/2) = O(n)

# Rule: For interviews, usually focus on WORST case
```

---

# COMMON COMPLEXITIES

## Python Built-in Operations

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| list[i] | O(1) | - | Direct index access |
| list.append() | O(1)* | - | * Amortized |
| list.insert(i) | O(n) | - | Shifts elements |
| list.remove() | O(n) | - | Must find, then shift |
| list.pop() | O(1) | - | Last element |
| list.pop(i) | O(n) | - | Shifts after removal |
| sorted(list) | O(n log n) | O(n) | |
| list.sort() | O(n log n) | O(1) | In-place |
| dict[key] | O(1)* | - | Average case |
| dict.update() | O(n) | O(n) | n = size of dict |
| set.add() | O(1)* | - | Average case |
| set.remove() | O(1)* | - | Average case |
| len() | O(1) | - | Pre-computed |
| sum() | O(n) | - | Must iterate |
| max() | O(n) | - | Must compare all |

---

# SPACE COMPLEXITY

## What is Space Complexity?

**Definition:** How much additional memory an algorithm uses relative to input size

**Note:** Space usually refers to ADDITIONAL space, not including input

```python
def find_max(arr):
    max_val = arr[0]  # O(1) - one variable
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Space Complexity: O(1) - uses only max_val variable
# Does NOT count the input array arr
```

---

## O(1) - Constant Space

```python
def find_pair_sum(arr, target):
    for i in range(len(arr)):
        complement = target - arr[i]  # One variable
        for j in range(i+1, len(arr)):
            if arr[j] == complement:
                return (arr[i], arr[j])  # One variable
    return None

# Space: O(1) - only stores: complement, i, j
```

---

## O(n) - Linear Space

```python
def create_squared(arr):
    result = []  # New array of size n
    for num in arr:
        result.append(num ** 2)
    return result

# Space: O(n) - result array stores n elements
```

---

## O(n²) - Quadratic Space

```python
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)  # n×n matrix = n² elements
        matrix.append(row)
    return matrix

# Space: O(n²) - matrix contains n² elements
```

---

## Time vs Space Trade-off

```python
# Time: O(n²), Space: O(1)
def find_pair_sum_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# Time: O(n), Space: O(n)
def find_pair_sum_fast(arr, target):
    seen = {}  # Use extra space
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

# Better time, costs more space
# This trade-off is common in DSA!
```

---

# COMPARING ALGORITHMS

## When Does Each Complexity Matter?

```
n = 100:
O(n²) = 10,000 ops
O(n log n) = 664 ops
Difference: 15x slower (barely noticeable)

n = 10,000:
O(n²) = 100,000,000 ops
O(n log n) = 132,877 ops
Difference: 750x slower (starts to matter)

n = 1,000,000:
O(n²) = 1,000,000,000,000 ops (1 trillion!)
O(n log n) = 19,931,569 ops
Difference: 50,000x slower (MASSIVE!)

INSIGHT: Complexity matters more for large inputs
```

## Decision Tree: Which Algorithm?

```
Problem size n:
    ├─ n ≤ 10
    │  └─ Any algorithm works (even O(n!))
    │
    ├─ n ≤ 100
    │  └─ O(n²), O(n³) acceptable
    │
    ├─ n ≤ 1,000
    │  └─ O(n²) acceptable, O(n log n) preferred
    │
    ├─ n ≤ 1,000,000
    │  └─ O(n log n) required
    │  └─ O(n) preferred
    │
    └─ n > 1,000,000
       └─ O(n) or O(1) required
       └─ O(log n) bonus if possible
```

---

# WORKED EXAMPLES

## Example 1: Analyzing Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Complexity Analysis:**
```
Input: arr of size n

Line 1: for loop
├─ Runs: 0 to n-1 iterations
├─ In best case: 1 iteration (found at start)
├─ In worst case: n iterations (not found or at end)
├─ In average case: n/2 iterations

Line 2: Comparison (O(1))
├─ Constant time operation
├─ Doesn't depend on n

Line 3: Return (O(1))

Time Complexity:
├─ Best case: O(1) - found immediately
├─ Worst case: O(n) - need to check all elements
├─ Average case: O(n) - typically half the array
└─ For interviews: Report O(n)

Space Complexity: O(1)
└─ Uses only: i variable
```

---

## Example 2: Analyzing Binary Search

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
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

**Complexity Analysis:**
```
Input: arr of size n (MUST BE SORTED!)

Variables (O(1)):
├─ left, right, mid: constant space

While loop:
├─ Search space halves each iteration
├─ Iterations: log₂(n)
├─ Each iteration: O(1) operations

Time Complexity:
├─ Best case: O(1) - found at midpoint
├─ Worst case: O(log n) - halving until size 1
├─ Average case: O(log n)
└─ For interviews: Report O(log n)

Space Complexity: O(1)
```

**Why log n?**
```
Array size: 1,000,000
Iteration 1: 1,000,000 / 2 = 500,000
Iteration 2: 500,000 / 2 = 250,000
Iteration 3: 250,000 / 2 = 125,000
...
Iteration 20: 1

Total iterations: 20 ≈ log₂(1,000,000)
```

---

## Example 3: Analyzing Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Complexity Analysis:**
```
Input: arr of size n

Outer loop (i):
├─ Runs n times (0 to n-1)

Inner loop (j):
├─ Iteration i=0: (n-1) comparisons
├─ Iteration i=1: (n-2) comparisons
├─ Iteration i=2: (n-3) comparisons
├─ ...
├─ Iteration i=n-1: 0 comparisons
├─ Total: (n-1) + (n-2) + ... + 1 + 0

Summation:
├─ Sum from 1 to (n-1) = n(n-1)/2
├─ = (n² - n)/2
├─ ≈ n²/2 for large n

Time Complexity:
├─ Best case: O(n) - already sorted (with optimization)
├─ Worst case: O(n²) - reverse sorted
├─ Average case: O(n²)
└─ For interviews: Report O(n²)

Space Complexity: O(1)
└─ Sorts in-place
```

---

# COMPLEXITY PROOFS

## Proof: n + n = O(n) NOT O(2n)

**We need to show:** $n + n = O(n)$

**Proof:**
$$n + n = 2n$$

We need constants $c > 0$ and $n_0 > 0$ such that:
$$2n \leq c \cdot n \text{ for all } n \geq n_0$$

Choose $c = 3$ and $n_0 = 1$:
$$2n \leq 3 \cdot n \quad \checkmark \text{ (true for all } n \geq 1\text{)}$$

Therefore: $n + n = O(n)$

**Key insight:** Constant factors are ignored in Big O

---

## Proof: n² + n = O(n²) NOT O(n)

**We need to show:** $n^2 + n = O(n^2)$

**Proof:**
$$n^2 + n \leq n^2 + n^2 = 2n^2 \quad (\text{for } n \geq 1)$$

So choose $c = 2$ and $n_0 = 1$:
$$n^2 + n \leq 2 \cdot n^2 \quad \checkmark$$

Therefore: $n^2 + n = O(n^2)$

**Key insight:** Lower-order terms are dominated by higher-order terms

---

## Proof: log₂(n) = O(log₁₀(n))

**We need to show:** $\log_2(n) = O(\log_{10}(n))$

**Proof using change of base:**
$$\log_2(n) = \frac{\log_{10}(n)}{\log_{10}(2)} = \frac{\log_{10}(n)}{0.301} \approx 3.32 \cdot \log_{10}(n)$$

Choose $c = 3.32$ and $n_0 = 1$:
$$\log_2(n) \leq 3.32 \cdot \log_{10}(n) \quad \checkmark$$

Therefore: $\log_2(n) = O(\log_{10}(n))$

**Key insight:** Logarithm base doesn't matter in Big O
(all logarithms grow at same rate)

---

# PRACTICE PROBLEMS

## Easy: Identify Complexity

### Problem 1
```python
def problem1(arr):
    return arr[0]

# Answer: O(1)
# Reason: Direct array access, no loops
```

### Problem 2
```python
def problem2(arr):
    for num in arr:
        print(num)

# Answer: O(n)
# Reason: Single loop through n elements
```

### Problem 3
```python
def problem3(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i] + arr[j])

# Answer: O(n²)
# Reason: Nested loops, n × n iterations
```

---

## Medium: Analyze Complex Code

### Problem 4
```python
def problem4(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

# Answer: O(n²)
# Reason: Two nested loops, body is O(1)
# This is a selection sort variant
```

### Problem 5
```python
def problem5(arr):
    # First loop: O(n)
    for num in arr:
        print(num)
    
    # Second set of loops: O(n²)
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# Answer: O(n²)
# Reason: O(n) + O(n²) = O(n²)
# (Maximum dominates)
```

---

## Hard: Optimize Complexity

### Problem 6 - Find Duplicate

**Current Solution:** O(n²)
```python
def find_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

**Optimized Solution:** O(n)
```python
def find_duplicate_fast(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Analysis:**
- Slow: Two nested loops = O(n²)
- Fast: Single loop + hash set = O(n)
- Trade-off: Use O(n) space to save time

---

# INTERVIEW PREPARATION

## Key Interview Questions

**Q1: Explain Big O notation**
```
A: Big O describes how algorithm time/space scales with input.
   O(n) means proportional to input size.
   O(n²) means quadratic - 4x slower when input doubles.
   
   We care about WORST case for interviews.
```

**Q2: What's the difference between O(n) and O(2n)?**
```
A: They're the same!
   O(2n) = O(n) because constant factors are ignored.
   Both are O(n).
   
   Rule: For large n, constants don't matter.
   2n ≈ n for huge n
```

**Q3: Why is logarithm important?**
```
A: Logarithm means problem size is cut in half each step.
   log₂(1,000,000) ≈ 20
   
   So 20 steps reduce problem from 1M to 1.
   Binary search is O(log n) - extremely fast!
```

**Q4: How do you optimize O(n²) to O(n)?**
```
A: Common techniques:
   1. Use hash map/set - trade space for time
   2. Sort first - enables two-pointer approach
   3. Divide and conquer - reduce problem recursively
   
   Example: Two-sum problem
   Brute: O(n²) - check all pairs
   Optimized: O(n) - use hash map to track seen numbers
```

---

## Complexity Cheat Sheet

**Remember These:**
```
O(1):       Instant (dict access, array indexing)
O(log n):   Binary search, balanced BST
O(n):       Linear search, single loop
O(n log n): Good sorting, most interviews expect this
O(n²):      Nested loops, acceptable for n < 1000
O(2^n):     AVOID! Only for n ≤ 20
O(n!):      NEVER! Only for n ≤ 10
```

**Common Patterns:**
```
Single loop:           O(n)
Nested loops:          O(n²)
Divide and conquer:    O(n log n)
Halving each time:     O(log n)
```

---

**Master Big O. It's 50% of DSA interviews.** 🎯

