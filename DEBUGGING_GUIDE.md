# 🔍 Debugging Guide for DSA Code

**"My code doesn't work. What now?"**

Systematic debugging approach to fix any DSA bug in minutes, not hours.

---

## 🚀 The Debugging Framework

### Step 1: Understand What "Broken" Means (2 min)

**Is your code:**
- [ ] **Not running?** (Syntax error, import error, crash)
- [ ] **Running but wrong answer?** (Logic error)
- [ ] **Running but too slow?** (Efficiency problem)
- [ ] **Running but memory error?** (Space issue)
- [ ] **Running but getting partial credit?** (Edge cases)

---

### Step 2: Gather Information (3 min)

#### For "Not Running":
```python
# Error message - READ IT CAREFULLY
Traceback (most recent call last):
  File "solution.py", line 15, in <module>
    result = solution([1, 2, 3])
  File "solution.py", line 8, in solution
    return arr[index]  # <- Line causing error
IndexError: list index out of range
```

**Action:** Go to line mentioned. Understand what caused it.

#### For "Wrong Answer":
```python
# Your output vs Expected
Your output: [1, 2, 4]
Expected:    [1, 2, 3]
```

**Action:** Find first difference. Why did you produce 4 instead of 3?

#### For "Time Limit Exceeded":
```python
# Your complexity
Your algorithm: O(n²) for n = 100,000
Time: 100,000² = 10,000,000,000 operations
Limit: Usually 10⁸ operations = 1 second
Your code: 100 seconds - TIMEOUT!
```

**Action:** Need to optimize. Check PATTERN_RECOGNITION_GUIDE.md for better approach.

---

## 🔴 Debugging "Not Running" (Crash)

### Common Crashes & Solutions

#### 1. IndexError: list index out of range
```python
# ❌ Problem
arr = [1, 2, 3]
print(arr[5])  # IndexError!

# ✅ Solution 1: Check bounds
if index < len(arr):
    print(arr[index])

# ✅ Solution 2: Use safe access
try:
    print(arr[index])
except IndexError:
    print("Index out of bounds")

# ✅ Solution 3: Understand your indexing
# If arr = [1, 2, 3], valid indices are 0, 1, 2
# To avoid this: Always use index < len(arr)
```

**Prevention:** Before accessing arr[i], verify i >= 0 and i < len(arr)

---

#### 2. RecursionError: maximum recursion depth exceeded
```python
# ❌ Problem
def factorial(n):
    return n * factorial(n - 1)  # No base case!

# Causes infinite recursion

# ✅ Solution: Add base case FIRST
def factorial(n):
    if n <= 1:  # BASE CASE
        return 1
    return n * factorial(n - 1)

# ✅ Solution 2: Check for infinite recursion
# Always ask: "When does recursion stop?"
# If you can't answer, you're missing a base case
```

**Prevention:** Base case ALWAYS comes before recursive call.

---

#### 3. TypeError: unhashable type: 'list'
```python
# ❌ Problem
d = {}
d[[1, 2, 3]] = "value"  # TypeError! Lists aren't hashable

# ✅ Solution: Use hashable type
d = {}
d[(1, 2, 3)] = "value"  # Tuples ARE hashable

# ✅ Solution 2: For sets too
s = set()
s.add((1, 2, 3))  # Works with tuple
s.add([1, 2, 3])  # Fails - TypeError
```

**Prevention:** Hash map keys and set items must be hashable (int, str, tuple, not list/dict).

---

#### 4. KeyError: dictionary key missing
```python
# ❌ Problem
d = {"a": 1, "b": 2}
print(d["c"])  # KeyError!

# ✅ Solution 1: Check key exists
if "c" in d:
    print(d["c"])
else:
    print("Key not found")

# ✅ Solution 2: Use get() with default
print(d.get("c", "default_value"))

# ✅ Solution 3: Use defaultdict
from collections import defaultdict
d = defaultdict(int)  # Defaults to 0
print(d["c"])  # Returns 0, no error
```

**Prevention:** Check if key exists before accessing. Or use .get() or defaultdict.

---

#### 5. NameError: name not defined
```python
# ❌ Problem
print(variable_name)  # NameError: name not defined

# Causes:
# 1. Typo in variable name
# 2. Scope issue (defined in function, used outside)
# 3. Defined later in code but used before

# ✅ Solution: Check spelling, scope, order
```

**Prevention:** Define before using. Watch for typos.

---

## 🟠 Debugging "Wrong Answer" (Logic Error)

### The 5-Step Process

#### Step 1: Simplify Input (Reduce, Reduce, Reduce)
```python
# If your 100-element test fails, try:
# -> 10-element test
# -> 5-element test
# -> 3-element test
# -> 1-element test
# -> empty input

# Find SMALLEST input that fails. Debug that.
```

#### Step 2: Trace Execution by Hand
```python
# Example: Find maximum in array
def find_max(arr):
    max_val = 0  # BUG: Should be float('-inf')
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Test with [-5, -3, -1]
# Your code: max_val = 0 (wrong! -1 is max)
# Expected: -1

# Trace:
# max_val = 0
# num = -5: -5 > 0? No, max_val = 0
# num = -3: -3 > 0? No, max_val = 0
# num = -1: -1 > 0? No, max_val = 0
# Return 0 - WRONG!

# Found bug: Initial value should be arr[0] or float('-inf')
```

**Pro Tip:** Trace 2-3 simple examples by hand. Most bugs reveal themselves.

---

#### Step 3: Add Print Statements (Print Debugging)
```python
# Add prints to see what's happening
def solution(arr, target):
    print(f"Input: arr={arr}, target={target}")
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        print(f"left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Found at {mid}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print(f"Not found")
    return -1

# Run and see exactly what's happening at each step
```

**When to use:** When trace-by-hand isn't enough. Print key variables at critical points.

---

#### Step 4: Use Debugger (Professional Approach)
```python
# VS Code Debugging:
# 1. Set breakpoint (click left of line number)
# 2. Run with debugger (F5 or Run menu)
# 3. Inspect variables
# 4. Step through execution (F10)
# 5. See exactly what went wrong

# Python REPL debugging:
import pdb
def solution(arr, target):
    pdb.set_trace()  # Execution pauses here
    # Now inspect variables, step through
    ...
```

**When to use:** For complex bugs. See execution step-by-step.

---

#### Step 5: Check Edge Cases
```python
# If regular test passes but edge case fails:

# Empty input
arr = []
print(solution(arr, 5))  # Should handle gracefully

# Single element
arr = [5]
print(solution(arr, 5))  # Should return 0 or True

# All same elements
arr = [5, 5, 5, 5]
print(solution(arr, 5))  # Should handle duplicates

# Negative numbers
arr = [-5, -3, 0, 3, 5]
print(solution(arr, -5))  # Should work with negatives

# All false cases
arr = [1, 2, 3]
print(solution(arr, 10))  # Should return -1 or False

# Large input
arr = list(range(10000))
print(solution(arr, 9999))  # Should not timeout
```

**Most bugs:** Are in edge cases. Test them explicitly.

---

## 🟡 Debugging "Too Slow" (Efficiency)

### Complexity Analysis Checklist

```python
# For each operation in code, ask: "What's the complexity?"

def solution(arr, target):
    # arr.sort() - O(n log n)
    arr.sort()
    
    # for loop - O(n) iterations
    for i in range(len(arr)):
        # arr.index(target) - O(n) operation in a loop!
        if arr.index(target - arr[i]) != -1:  # DON'T DO THIS!
            return [i, arr.index(target - arr[i])]
    
    # Total: O(n log n) + O(n) * O(n) = O(n²) - TOO SLOW!
```

**Better approach:**
```python
def solution(arr, target):
    # Sort - O(n log n)
    arr.sort()
    
    # Two pointers - O(n)
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    
    # Total: O(n log n) - Fast!
```

### Common Slow Patterns

| Pattern | Complexity | Example | Fix |
|---------|-----------|---------|-----|
| **Nested loops** | O(n²) | for i in range(n): for j in range(n) | Use hash map, two pointers, or sorting |
| **.index() in loop** | O(n²) | for x in arr: if target-x in arr | Use hash set instead: if target-x in hash_set |
| **.remove() in loop** | O(n²) | while len(arr) > 0: arr.remove(x) | Iterate backwards or list comprehension |
| **Recursion without memo** | O(2^n) | fibonacci(n) | Use memoization (cache results) |
| **Regenerating data** | O(n²+) | Building same graph multiple times | Build once, reuse |

**Solution:** Profile your code. Find slowest operation. Optimize that.

---

## 🟢 Debugging "Memory Error" (Space)

### Common Memory Issues

```python
# ❌ Creating huge intermediate list
def solution(n):
    result = list(range(n * 1000000))  # 1 billion elements!
    # MemoryError for n > 1000

# ✅ Use generator instead
def solution(n):
    result = (i for i in range(n * 1000000))  # Lazy evaluation
    # No memory error!

# ❌ Deep recursion creates stack frames
def recursion(n):
    if n == 0:
        return 0
    return recursion(n - 1)

recursion(10000)  # RecursionError: Too deep!

# ✅ Increase recursion limit (carefully!)
import sys
sys.setrecursionlimit(20000)
recursion(10000)  # Now works (but still risky)

# ✅ Better: Convert to iteration
def iterative(n):
    result = 0
    for i in range(n):
        result += 1  # No recursion, no stack growth
    return result
```

**Rule:** If using too much memory, look for large lists/recursion depth.

---

## 🎯 Debugging Decision Tree

```
My code is broken!
    ↓
Does it run?
├─ NO (Crash)
│   ├─ Error at line X?
│   │   ├─ IndexError → Check bounds (index < len)
│   │   ├─ RecursionError → Add base case
│   │   ├─ TypeError → Use right type (tuple not list)
│   │   ├─ KeyError → Check key exists
│   │   └─ NameError → Check spelling/scope
│   └─ → Add try-except to isolate
│
└─ YES (Runs)
    ├─ Wrong answer?
    │   ├─ Simplify input
    │   ├─ Trace by hand
    │   ├─ Add print statements
    │   ├─ Test edge cases
    │   └─ → Found bug? Fix and re-test
    │
    ├─ Too slow?
    │   ├─ Analyze complexity
    │   ├─ Find O(n²) or O(2^n) operations
    │   ├─ Use hash map, sorting, or pointers
    │   └─ → Implement faster approach
    │
    └─ Memory error?
        ├─ Find large allocations
        ├─ Use generators instead of lists
        ├─ Reduce recursion depth
        └─ → Optimize memory usage
```

---

## 💡 Debugging Pro Tips

### Tip 1: Print the Problem Itself
```python
# Before debugging, understand what you're solving
def solution(nums):
    print(f"Problem: Find max in {nums}")
    # Now you're clear on what you're doing
```

### Tip 2: Test with Provided Examples First
```python
# ALWAYS test provided examples
# If they pass but hidden tests fail, it's an edge case

def solution(arr, target):
    # Test 1: arr = [1,3,5,6], target = 5 -> 2
    assert solution([1,3,5,6], 5) == 2
    
    # Test 2: arr = [1,3,5,6], target = 7 -> 4
    assert solution([1,3,5,6], 7) == 4
    
    # If these pass, debug edge cases
    # Edge: arr = [], target = 1
    # Edge: arr = [1], target = 0
```

### Tip 3: Isolate the Problem
```python
# If solution is complex, test pieces separately

def solution(arr, target):
    # Test sorting
    sorted_arr = sorted(arr)
    print(f"Sorted: {sorted_arr}")
    assert sorted_arr == sorted(arr)
    
    # Test searching
    result = binary_search(sorted_arr, target)
    print(f"Result: {result}")
    
    # Test combination
    return result

# Now you know which part fails
```

### Tip 4: Use Assertions
```python
# Assert your assumptions
def solution(arr, target):
    assert len(arr) > 0, "Array cannot be empty"
    assert isinstance(arr, list), "Must be a list"
    assert all(isinstance(x, int) for x in arr), "All elements must be ints"
    
    # Code fails early with clear message if assumptions violated
```

### Tip 5: Compare with Brute Force
```python
# If optimized solution fails, compare with brute force

def brute_force(arr, target):
    # Simple, obviously correct (maybe slow)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

def optimized(arr, target):
    # Fast but potentially buggy
    ...

# Test both on same inputs
# If brute force and optimized differ, find where
```

### Tip 6: Read the Error Message Carefully
```python
# ❌ "Something went wrong"
# ✅ "IndexError: list index out of range at line 15"

# The error message tells you:
# 1. What went wrong (IndexError)
# 2. Where (line 15)
# 3. Why (list index out of range)

# Always read the full error message!
```

---

## 🚀 The 10-Minute Debug Process

**If your code isn't working, do this:**

1. **Read the error** (1 min) - What does error message say?
2. **Find the line** (1 min) - Go to line number in error
3. **Understand the line** (2 min) - What should it do? Why did it fail?
4. **Check inputs** (2 min) - Are inputs what you expect?
5. **Test edge case** (2 min) - Does this fail on empty/single/large input?
6. **Fix and re-run** (2 min) - Try solution, test again
7. **Verify fix** (2 min) - Works on other tests too?

**If not fixed after 10 minutes, take a break. Fresh perspective helps!**

---

## ✅ Debugging Checklist

Before giving up:
- [ ] Read error message completely
- [ ] Checked line causing error
- [ ] Tested with smallest possible input
- [ ] Traced execution by hand
- [ ] Added print statements
- [ ] Tested all edge cases
- [ ] Checked complexity
- [ ] Compared with brute force
- [ ] Used debugger
- [ ] Checked COMMON_MISTAKES.md for similar issue

---

**Remember: Every bug has a reason. Systematic debugging finds it.** 🎯

