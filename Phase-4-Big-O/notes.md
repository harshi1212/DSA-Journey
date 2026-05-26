# Phase 4 - Big O Complexity Analysis

## What is it?

Big O is how we measure algorithm efficiency:
- **Time Complexity** → How fast does it run? (as input gets larger)
- **Space Complexity** → How much memory does it use?

Instead of saying "takes 5 seconds", we describe growth rate: O(n), O(n²), O(log n), etc.

---

## Why does it matter?

**Real-world reasons:**
1. **Scaling matters** - Your code works on 10 items. What about 1,000,000?
2. **Interview essential** - First question is always "What's the complexity?"
3. **Choose right algorithm** - O(n) solution beats O(n²) by 1000x
4. **System design** - Can't ignore complexity at scale
5. **Competition** - Online judges have time limits (usually 1-2 seconds)

---

## Common Complexities (Best to Worst)

```
O(1)       - Constant time (always same speed) ✅ BEST
O(log n)   - Logarithmic (binary search)
O(n)       - Linear (loop through each item)
O(n log n) - Linearithmic (merge sort, quicksort)
O(n²)      - Quadratic (nested loops)
O(n³)      - Cubic (triple nested loops)
O(2ⁿ)      - Exponential (recursive without memoization) 🔴 WORST
O(n!)      - Factorial (permutations)
```

---

## How to Calculate Big O

```
Ignore constants: O(2n) = O(n)
Ignore lower terms: O(n² + n) = O(n²)
Nested loops multiply: O(n) inside O(n) = O(n²)
Sequential loops add: O(n) + O(m) = O(n + m)
```

---

## Python Implementation

### Time Complexity Examples

```python
# O(1) - Constant time
def get_first(arr):
    return arr[0]  # Always takes same time, no matter arr size

# O(n) - Linear time
def print_all(arr):
    for item in arr:
        print(item)  # If arr has 10 items, 10 operations
                     # If arr has 100 items, 100 operations

# O(n²) - Quadratic time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # For n items, n×n operations

# O(log n) - Logarithmic time
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

# O(n log n) - Linearithmic time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

### Space Complexity Examples

```python
# O(1) - Constant space
def get_sum(arr):
    total = 0  # Only one variable, no matter arr size
    for num in arr:
        total += num
    return total

# O(n) - Linear space
def create_copy(arr):
    return arr.copy()  # Creates new array of same size

# O(n) - Space for recursion stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Stack grows n levels deep
```

---

## Common Mistakes Beginners Make

1. **Counting operations instead of analyzing growth**
   - ❌ Wrong: "This runs 5 operations so it's O(5)"
   - ✅ Right: "As input grows, it takes 2×n operations, so O(n)"

2. **Confusing loop with complexity**
   - ❌ Wrong: One loop = O(n), two loops = O(2n) [which is still O(n)]
   - ✅ Right: One loop = O(n), nested loops = O(n²)

3. **Ignoring hidden complexities**
   - ❌ Wrong: Assuming `.append()` is O(1) without checking implementation
   - ✅ Right: Know that list operations vary in complexity

4. **Not considering space for recursion**
   - ❌ Wrong: Only counting return values, ignoring call stack
   - ✅ Right: Recursion depth = O(n) space

5. **Mixing space and time complexity**
   - ❌ Wrong: "This is O(n²)" without specifying if time or space
   - ✅ Right: "Time: O(n²), Space: O(1)"

6. **Forgetting about hidden loops**
   - ❌ Wrong: Not counting loops inside library functions
   - ✅ Right: `.sort()` is O(n log n), affects total complexity

---

## How to know I understand this

Checklist:
- [ ] I can identify time complexity from code without counting steps
- [ ] I understand O(n²) is worse than O(n log n) for large n
- [ ] I can write O(log n) solution using binary search
- [ ] I know space complexity of recursion comes from call stack
- [ ] I can compare two algorithms and say which is faster for large input
- [ ] I can solve Big O question from interview

---

## Practice Problems

- Easy: [Valid Palindrome — LeetCode #125](https://leetcode.com/problems/valid-palindrome/) (analyze your solution's complexity)
- Easy: [Two Sum — LeetCode #1](https://leetcode.com/problems/two-sum/) (compare O(n²) vs O(n))
- Medium: [Search in Rotated Sorted Array — LeetCode #33](https://leetcode.com/problems/search-in-rotated-sorted-array/) (O(log n) challenge)
