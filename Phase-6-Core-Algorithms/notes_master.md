# Phase 6 - Core Algorithms (Complete Master Guide)

**Build algorithmic thinking. These algorithms solve 60% of real problems.**

---

## Table of Contents
1. [Recursion Theory](#recursion-theory)
2. [Sorting Algorithms](#sorting-algorithms)
3. [Searching Algorithms](#searching-algorithms)
4. [Algorithm Analysis Techniques](#algorithm-analysis-techniques)
5. [Worked Examples (50+)](#worked-examples)
6. [Interview Preparation](#interview-preparation)

---

# RECURSION THEORY

## Formal Definition

**Definition:** Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.

**Mathematical Definition:**
```
A recursive function f is defined in terms of:
1. Base case(s): f(n) = value (where recursion stops)
2. Recursive case: f(n) = f(n-1) or f(n-2) or ...
   (where function calls itself with smaller input)

For all n ≥ n_min, the sequence f(n), f(n-1), ... must reach base case.
```

---

## Understanding Recursion with Call Stack

```python
def countdown(n):
    print(f"countdown({n})")
    if n == 0:              # Base case
        print("Done!")
        return
    countdown(n - 1)        # Recursive call
    print(f"Return from countdown({n})")

countdown(3)
```

**Execution Trace - Call Stack:**
```
countdown(3)
│  print "countdown(3)"
│  n != 0, so call countdown(2)
│
├─ countdown(2)
│  │  print "countdown(2)"
│  │  n != 0, so call countdown(1)
│  │
│  ├─ countdown(1)
│  │  │  print "countdown(1)"
│  │  │  n != 0, so call countdown(0)
│  │  │
│  │  ├─ countdown(0)
│  │  │  │  print "countdown(0)"
│  │  │  │  n == 0, BASE CASE REACHED
│  │  │  │  print "Done!"
│  │  │  │  return
│  │  │  │
│  │  │  print "Return from countdown(1)"
│  │  │  return
│  │  │
│  │  print "Return from countdown(2)"
│  │  return
│  │
│  print "Return from countdown(3)"
│  return

Output:
countdown(3)
countdown(2)
countdown(1)
countdown(0)
Done!
Return from countdown(1)
Return from countdown(2)
Return from countdown(3)
```

---

## Recursion Types

### Type 1: Linear Recursion

**Definition:** Each recursive call makes exactly 1 recursive call

```python
def factorial(n):
    if n <= 1:           # Base case
        return 1
    return n * factorial(n - 1)  # 1 recursive call

# Call tree:
# factorial(5)
# └─ factorial(4)
#    └─ factorial(3)
#       └─ factorial(2)
#          └─ factorial(1) [base case]

# Time: O(n) - n recursive calls
# Space: O(n) - call stack depth = n
```

### Type 2: Binary Recursion

**Definition:** Each recursive call makes exactly 2 recursive calls

```python
def fibonacci(n):
    if n <= 1:                    # Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # 2 recursive calls

# Call tree:
#          fib(5)
#         /      \
#      fib(4)    fib(3)
#      /    \    /    \
#   fib(3) fib(2) fib(2) fib(1)
#   ...

# Time: O(2^n) - EXPONENTIAL!
# Space: O(n) - maximum call stack depth
```

### Type 3: Multiple Recursion

**Definition:** Each recursive call may make multiple recursive calls

```python
def sum_all_paths(node):
    if node is None:
        return 0
    total = node.val
    for child in node.children:          # Multiple recursive calls
        total += sum_all_paths(child)
    return total
```

---

## Recursion Analysis with Recurrence Relations

### Example 1: Linear Search

```python
def linear_search_recursive(arr, target, index=0):
    if index == len(arr):           # Base case
        return -1
    if arr[index] == target:        # Base case
        return index
    return linear_search_recursive(arr, target, index + 1)  # Recursive

# Recurrence Relation:
# T(n) = T(n-1) + O(1)    for n > 0
# T(0) = O(1)
#
# Solving:
# T(n) = T(n-1) + 1
#      = T(n-2) + 1 + 1
#      = T(n-3) + 1 + 1 + 1
#      = ...
#      = T(0) + n
#      = n
#
# Therefore: T(n) = O(n)
```

### Example 2: Naive Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Recurrence Relation:
# T(n) = T(n-1) + T(n-2) + O(1)
# T(0) = O(1)
# T(1) = O(1)
#
# This is the Fibonacci recurrence itself!
# Solution: T(n) = O(2^n)  [approximately O(φ^n) where φ ≈ 1.618]
```

---

## Memoization: Optimizing Recursive Solutions

**Problem:** Fibonacci computes same subproblems repeatedly

```python
# Naive: O(2^n)
fib(5) calls fib(4) and fib(3)
fib(4) calls fib(3) and fib(2)
        ↑ fib(3) computed TWICE!
```

**Solution: Memoization (cache results)**

```python
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:           # Check cache first
        return memo[n]
    
    if n <= 1:
        return n
    
    result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    memo[n] = result        # Store in cache
    return result

# Analysis:
# Subproblems: fib(0), fib(1), ..., fib(n) = n+1 subproblems
# Each computed once: O(1) per subproblem
# Total: O(n) time, O(n) space
```

---

# SORTING ALGORITHMS

## Sorting Fundamentals

**Definition:** Sorting is arranging elements in non-decreasing (or non-increasing) order.

**Sorting Problem:**
```
Input: Array [a₀, a₁, ..., aₙ₋₁]
Output: Array [a'₀, a'₁, ..., a'ₙ₋₁]

Where: a'₀ ≤ a'₁ ≤ ... ≤ a'ₙ₋₁

AND: output is permutation of input
```

---

## Bubble Sort

**Algorithm:** Repeatedly swap adjacent elements if they're out of order

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:     # Optimization: stop if sorted
            break
    return arr
```

**Execution Trace:**
```
Initial: [5, 2, 4, 1]

Pass 1 (largest bubbles to end):
  Compare 5,2: swap → [2, 5, 4, 1]
  Compare 5,4: swap → [2, 4, 5, 1]
  Compare 5,1: swap → [2, 4, 1, 5]  ← 5 in position

Pass 2 (second-largest bubbles):
  Compare 2,4: no swap → [2, 4, 1, 5]
  Compare 4,1: swap → [2, 1, 4, 5]  ← 4 in position

Pass 3 (third-largest):
  Compare 2,1: swap → [1, 2, 4, 5]  ← 2 in position

Pass 4: Already sorted

Final: [1, 2, 4, 5]
```

**Complexity Analysis:**
```
Time:
- Best case: O(n) - if already sorted (with optimization)
- Average case: O(n²) - random order
- Worst case: O(n²) - reverse sorted

Proof of worst case:
Pass 1: n-1 comparisons
Pass 2: n-2 comparisons
Pass 3: n-3 comparisons
...
Pass n: 0 comparisons

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²)

Space: O(1) - sorts in place
Stable: Yes - equal elements maintain relative order
```

---

## Selection Sort

**Algorithm:** Find minimum, place at beginning, repeat for rest

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Execution Trace:**
```
Initial: [5, 2, 4, 1]

Find min of [5, 2, 4, 1]: 1 at index 3
Swap 5 and 1: [1, 2, 4, 5]

Find min of [2, 4, 5]: 2 at index 1
Swap with index 1: [1, 2, 4, 5] (no change)

Find min of [4, 5]: 4 at index 2
Swap with index 2: [1, 2, 4, 5] (no change)

Final: [1, 2, 4, 5]
```

**Complexity Analysis:**
```
Time:
- Best/Average/Worst: O(n²)
  
Proof:
Pass 1: Find min in n elements = n-1 comparisons
Pass 2: Find min in n-1 elements = n-2 comparisons
...
Pass n: Find min in 1 element = 0 comparisons

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²)

Space: O(1) - sorts in place
Stable: No - swaps disturb order of equals
```

---

## Insertion Sort

**Algorithm:** Insert each element into correct position in sorted portion

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Execution Trace:**
```
Initial: [5, 2, 4, 1]

i=1: Insert 2 into [5]
  2 < 5, shift 5 right: [5, 5, 4, 1]
  Insert 2: [2, 5, 4, 1]

i=2: Insert 4 into [2, 5]
  4 < 5, shift 5 right: [2, 5, 5, 1]
  4 > 2, stop: [2, 4, 5, 1]

i=3: Insert 1 into [2, 4, 5]
  1 < 5, shift: [2, 4, 5, 5]
  1 < 4, shift: [2, 4, 4, 5]
  1 < 2, shift: [2, 2, 4, 5]
  Insert 1: [1, 2, 4, 5]

Final: [1, 2, 4, 5]
```

**Complexity Analysis:**
```
Time:
- Best: O(n) - already sorted (inner loop never runs)
- Average: O(n²)
- Worst: O(n²) - reverse sorted

Proof of worst case:
i=1: 1 comparison worst
i=2: 2 comparisons worst
...
i=n-1: n-1 comparisons worst

Total: 1 + 2 + ... + (n-1) = n(n-1)/2 = O(n²)

Space: O(1) - sorts in place
Stable: Yes - maintains relative order of equals
```

---

## Merge Sort

**Algorithm:** Divide array in half, sort each half, merge sorted halves

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Execution Trace:**
```
Initial: [5, 2, 4, 1]

Divide:
  [5, 2, 4, 1]
  /          \
[5, 2]       [4, 1]
/    \       /    \
[5]  [2]   [4]  [1]

Merge/Sort:
[5]  [2]   →  [2, 5]
[4]  [1]   →  [1, 4]

[2, 5]  [1, 4]  →  [1, 2, 4, 5]

Final: [1, 2, 4, 5]
```

**Complexity Analysis:**
```
Time: O(n log n) for all cases

Proof:
Divide array: log₂(n) levels
Each level: merge all elements = O(n)
Total: n × log₂(n) = O(n log n)

Space: O(n) - merge needs temporary array

Recurrence:
T(n) = 2·T(n/2) + n
     = 2·[2·T(n/4) + n/2] + n
     = 4·T(n/4) + n + n
     = ...
     = n·T(1) + n·log₂(n)
     = n + n·log₂(n)
     = O(n log n)

Stable: Yes
```

---

## Quick Sort

**Algorithm:** Partition array around pivot, recursively sort partitions

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# In-place version:
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Execution Trace:**
```
Initial: [5, 2, 4, 1, 8]
Pivot: 4

Partition around 4:
  Less: [2, 1]
  Equal: [4]
  Greater: [5, 8]

Recursively sort:
  Quick_sort([2, 1]) → [1, 2]
  Quick_sort([5, 8]) → [5, 8]

Combine: [1, 2] + [4] + [5, 8] = [1, 2, 4, 5, 8]
```

**Complexity Analysis:**
```
Time:
- Best: O(n log n) - balanced partition
- Average: O(n log n) - random pivot
- Worst: O(n²) - bad pivot (e.g., sorted array, pivot always smallest)

Proof of best case:
T(n) = 2·T(n/2) + n  (partition each half)
     = O(n log n)  (Master Theorem)

Space: O(log n) - recursion depth for balanced case
       O(n) - worst case (full recursion tree)

Stable: No (simple version)
```

---

## Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

**When to use each:**
- **Small arrays:** Insertion sort (simple, low overhead)
- **Nearly sorted:** Insertion sort or Bubble sort
- **Large arrays:** Merge sort (guaranteed O(n log n)) or Quick sort (average fast)
- **External data:** Merge sort (sequential access)
- **Need stability:** Merge sort or Insertion sort

---

# SEARCHING ALGORITHMS

## Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Complexity:** O(n) - must check each element

---

## Binary Search

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

**Complexity:** O(log n) - halve search space each iteration

**Requirement:** Array MUST be sorted!

---

# ALGORITHM ANALYSIS TECHNIQUES

## Master Theorem

Used to solve recurrence relations of form:
$$T(n) = a \cdot T(n/b) + f(n)$$

Where:
- $a$ = number of subproblems
- $n/b$ = size of each subproblem
- $f(n)$ = work to divide and combine

**Three Cases:**

### Case 1: f(n) is dominated by recursive calls
If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$:
$$T(n) = \Theta(n^{\log_b a})$$

**Example:** Merge sort
- $a = 2, b = 2, f(n) = n$
- $\log_b a = \log_2 2 = 1$
- $f(n) = n = O(n^1)$, not dominated
- → Continue to Case 2

### Case 2: f(n) is same order as recursive calls
If $f(n) = \Theta(n^{\log_b a})$:
$$T(n) = \Theta(n^{\log_b a} \log n)$$

**Example:** Merge sort
- $f(n) = n = \Theta(n^{\log_2 2}) = \Theta(n)$
- → $T(n) = \Theta(n \log n)$ ✓

### Case 3: f(n) dominates recursive calls
If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$:
$$T(n) = \Theta(f(n))$$

**Example:** $T(n) = 2 \cdot T(n/2) + n^2$
- $a = 2, b = 2, f(n) = n^2$
- $\log_b a = 1$, $f(n) = n^2 = \Omega(n^{1+1})$
- → $T(n) = \Theta(n^2)$

---

# WORKED EXAMPLES

## Example 1: Analyzing Factorial Recursion

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Analysis:
# Recursion depth: n
# Work per call: O(1) multiplication
# Total: n calls × O(1) = O(n)

factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
```

## Example 2: Implementing and Analyzing Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # T(n/2)
    right = merge_sort(arr[mid:])     # T(n/2)
    return merge(left, right)         # O(n)

# Recurrence: T(n) = 2·T(n/2) + O(n)
# Master Theorem: Case 2 → T(n) = O(n log n)
```

---

# INTERVIEW PREPARATION

## Key Questions

**Q1: Difference between sorting algorithms?**
```
A: 
- Bubble/Selection/Insertion: O(n²), good for small n
- Merge Sort: O(n log n), stable, needs O(n) space
- Quick Sort: O(n log n) average, O(n²) worst, faster in practice
```

**Q2: Why is binary search O(log n)?**
```
A: Halves search space each iteration
   n → n/2 → n/4 → n/8 → ... → 1
   Number of halvings: log₂(n)
```

**Q3: When to use recursion vs iteration?**
```
A: Recursion:
   - Natural for tree/graph problems
   - Cleaner code for divide-and-conquer
   
   Iteration:
   - Better space complexity (no call stack)
   - Faster in practice (less overhead)
```

---

**Master sorting and recursion. They're 35% of coding interviews.** 🎯

