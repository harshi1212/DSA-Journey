# ✅ Code Quality Checklist for DSA

**What separates good code from great code?**

Use this checklist before submitting ANY solution. Good code = +10% interview confidence.

---

## 📋 Pre-Submission Checklist

### Correctness (Must Have)
- [ ] **Test all examples** - Provided examples pass?
- [ ] **Test edge cases** - Empty, single element, all same, negatives?
- [ ] **Test large input** - Doesn't timeout or crash?
- [ ] **No syntax errors** - Code runs without crashing?
- [ ] **Correct output format** - Return type matches requirement?

### Clarity (Should Have)
- [ ] **Meaningful variable names** - `max_val` not `m`; `visited` not `v`?
- [ ] **Comments at complex logic** - Why this approach? Explain tricky lines?
- [ ] **Function has docstring** - Explain inputs, outputs, complexity?
- [ ] **Logical organization** - Related code grouped together?
- [ ] **No magic numbers** - Constants have names?

```python
# ❌ Bad code quality
def solve(nums):
    # Comments missing
    m = float('-inf')
    for n in nums:
        m = max(m, n)
    return m

# ✅ Good code quality
def find_max(nums):
    """
    Find maximum element in array.
    
    Args:
        nums: List of integers
    
    Returns:
        Maximum integer, or -inf if array empty
    
    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return float('-inf')
    
    max_value = nums[0]
    for num in nums[1:]:
        max_value = max(max_value, num)
    
    return max_value
```

### Efficiency (Performance)
- [ ] **Complexity documented** - O(time) and O(space) in comments?
- [ ] **No unnecessary operations** - Avoiding repeated calculations?
- [ ] **Appropriate data structures** - Using hash map, not linear search?
- [ ] **No nested loops** - O(n²) when O(n) possible?
- [ ] **Early termination** - Break when found instead of continuing?

```python
# ❌ Inefficient
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):  # Unnecessary - checking i again!
            if nums[i] + nums[j] == target:
                return [i, j]

# ✅ Efficient  
def two_sum(nums, target):
    # Time: O(n), Space: O(n)
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Robustness (Handles Edge Cases)
- [ ] **Empty input handled** - `if not arr: return ...`?
- [ ] **None/null handled** - Checking for None values?
- [ ] **Single element works** - Special case for n=1?
- [ ] **Duplicates handled** - Works with same elements?
- [ ] **Boundary conditions correct** - Off-by-one avoided?

```python
# ❌ Fragile code
def get_element(arr, index):
    return arr[index]  # Crashes on invalid index

# ✅ Robust code
def get_element(arr, index):
    """Safely get element with bounds checking."""
    if not arr:
        return None
    if not isinstance(index, int):
        raise TypeError("Index must be integer")
    if index < 0 or index >= len(arr):
        return None
    return arr[index]
```

### Best Practices (Interview Impressiveness)
- [ ] **Use built-in functions appropriately** - `sorted()`, `min()`, `max()` vs manual?
- [ ] **Pythonic code** - List comprehensions, enumerate, unpacking?
- [ ] **DRY principle** - No repeated code?
- [ ] **Functions for logic** - Helper functions for clarity?
- [ ] **Type hints** (Python 3.5+) - Functions have type annotations?

```python
# ❌ Not Pythonic
result = []
for i in range(len(arr)):
    if arr[i] > 0:
        result.append(arr[i])

# ✅ Pythonic
result = [x for x in arr if x > 0]

# Even better with type hints
def get_positives(arr: list[int]) -> list[int]:
    """Return positive numbers from array."""
    return [x for x in arr if x > 0]
```

---

## 🎯 Code Review Criteria

### Style Points

| Element | Good | Avoid |
|---------|------|-------|
| **Variable naming** | `max_height`, `num_islands` | `m`, `n`, `a`, `b` |
| **Function names** | `find_max`, `count_duplicates` | `f1`, `solve`, `main` |
| **Comments** | Explain WHY, not WHAT | `x = x + 1 # increment x` |
| **Spacing** | `result = [x for x in arr]` | `result=[x for x in arr]` |
| **Line length** | < 80-100 chars | > 100 chars (hard to read) |

### Documentation Points

```python
# ✅ Good documentation
def binary_search(arr: list[int], target: int) -> int:
    """
    Find target in sorted array using binary search.
    
    Algorithm: Standard binary search with two pointers
    
    Args:
        arr: Sorted list of integers
        target: Value to find
    
    Returns:
        Index of target, or -1 if not found
    
    Time Complexity: O(log n) - half array each iteration
    Space Complexity: O(1) - only two pointers
    
    Example:
        >>> binary_search([1, 3, 5, 7], 3)
        1
        >>> binary_search([1, 3, 5, 7], 4)
        -1
    """
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

---

## 🏆 Interview-Ready Code Template

```python
def solution(input_data) -> output_type:
    """
    [Clear one-sentence description of what problem solves]
    
    Approach:
    [Brief explanation of algorithm]
    
    Args:
        input_data: [Description of input]
    
    Returns:
        [Description of output]
    
    Time Complexity: O(...)
    Space Complexity: O(...)
    
    Example:
        >>> solution([example_input])
        expected_output
    """
    
    # Edge case handling
    if not input_data:
        return None
    
    # Main logic with clear sections
    # Section 1: Preparation
    # Section 2: Algorithm
    # Section 3: Post-processing (if needed)
    
    result = None
    
    # Comments for non-obvious logic
    for item in input_data:
        # Explanation of what happens here
        pass
    
    return result
```

---

## 📊 Code Quality Score

Rate your code 1-10:

**Correctness (40%)**
- 10: All tests pass, all edge cases handled
- 7: Tests pass, missing some edge cases
- 4: Wrong answer on some tests
- 1: Crashes or wrong format

**Clarity (30%)**
- 10: Crystal clear, excellent documentation
- 7: Clear with room for better comments
- 4: Hard to follow, unclear logic
- 1: Unreadable

**Efficiency (20%)**
- 10: Optimal complexity, no waste
- 7: Good complexity, minor improvements possible
- 4: Working but slow
- 1: Brute force, major optimization needed

**Robustness (10%)**
- 10: Handles all edge cases gracefully
- 7: Handles most edge cases
- 4: Missing edge case handling
- 1: Crashes on edge cases

**Score = (correctness × 0.4) + (clarity × 0.3) + (efficiency × 0.2) + (robustness × 0.1)**

**Target: 8.5+ before submitting to interview**

---

## 🔥 Red Flags (Code Smell)

If your code has ANY of these, improve before submitting:

- [ ] Duplicate code (copy-paste)
- [ ] 50+ line functions (too complex, break down)
- [ ] Deep nesting (> 3 levels)
- [ ] Too many parameters (> 4)
- [ ] No tests/examples
- [ ] No complexity analysis
- [ ] Magic numbers hardcoded
- [ ] Variables with single letters (`i, j, x, y` are OK for loops)
- [ ] No comments for complex logic
- [ ] Exception handling missing

---

## ✅ Final Submission Ritual

**Before hitting submit:**

1. **Run examples** - Does provided example work?
2. **Run edge cases** - Empty, single, large, negative?
3. **Check complexity** - Is it acceptable for constraints?
4. **Read code once more** - Any obvious bugs?
5. **Check formatting** - Consistent indentation, spacing?
6. **Verify comments** - Explain WHY at complex parts?
7. **Confirm types** - Input/output types correct?
8. **Test once more** - One final sanity check?

Only then: **Submit!**

---

## 💡 Pro Tips

### Tip 1: Explain While Coding
Write comments as you code, not after. It forces you to think through logic.

### Tip 2: Refactor, Don't Rewrite
If code works but ugly:
1. Keep original working version
2. Refactor piece by piece
3. Re-test after each change
4. Never rewrite from scratch mid-interview

### Tip 3: Balance Speed & Quality
- **In interviews**: Correct + explainable > Perfect + confusing
- **For practice**: Spend 20% extra on code quality. It compounds.

### Tip 4: Type Hints
```python
# Modern Python - use type hints
def max_subarray(nums: list[int]) -> int:
    ...

# Benefits:
# 1. Self-documenting
# 2. IDE can catch errors
# 3. Looks professional
```

### Tip 5: Use Assertions
```python
# Assert your assumptions
assert len(nums) > 0, "Array cannot be empty"
assert all(isinstance(x, int) for x in nums), "All elements must be ints"

# If wrong assumption, fail loudly immediately
```

---

## 🎓 Code Quality Levels

### Level 1: Beginner
- Code works
- Limited comments
- Obvious bugs possible
- No complexity analysis

### Level 2: Intermediate
- Code works on all tests
- Clear variable names
- Handles most edge cases
- Complexity analyzed

### Level 3: Advanced
- Everything from Level 2 +
- Documented with docstrings
- Type hints added
- Refactored for clarity
- DRY principle applied

### Level 4: Expert
- Everything from Level 3 +
- Handles all edge cases elegantly
- Multiple approaches considered
- Trade-offs explained
- Production-quality code

---

**Aim for Level 3-4 before interviews.** 

Practice quality now, interview success later! 💪

