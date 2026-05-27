# Phase 7 - Algorithm Patterns (Complete Master Guide)

**Most important phase for interviews. Master every pattern and you'll solve 70% of problems.**

---

## Table of Contents
1. [Pattern Recognition Framework](#pattern-recognition-framework)
2. [Two Pointers Pattern](#two-pointers-pattern)
3. [Sliding Window Pattern](#sliding-window-pattern)
4. [Binary Search Pattern](#binary-search-pattern)
5. [Dynamic Programming Pattern](#dynamic-programming-pattern)
6. [Backtracking Pattern](#backtracking-pattern)
7. [BFS/DFS Pattern](#bfsdfs-pattern)
8. [Greedy Pattern](#greedy-pattern)
9. [Sorting Patterns](#sorting-patterns)
10. [Pattern Decision Tree](#pattern-decision-tree)
11. [Worked Examples (60+)](#worked-examples)
12. [Interview Preparation](#interview-preparation)

---

# PATTERN RECOGNITION FRAMEWORK

## What is an Algorithm Pattern?

**Definition:** An algorithm pattern is a reusable solution template for a class of problems that share similar characteristics.

**Why Patterns Matter:**
```
Without patterns: Solve each problem from scratch (impossible!)
With patterns: Recognize pattern → Apply template → Solve

Benefit: Reduce 1000s of problems to 8-10 core patterns
```

---

## Pattern Decision Framework

```
Problem given? Ask these questions:

Q1: Do you need all elements?
├─ NO, only subset/optimal → Continue
└─ YES → Might be simple iteration

Q2: Can you modify input?
├─ YES (sort OK?) → Consider sorting
└─ NO → Must preserve input

Q3: Need to find something specific?
├─ Extreme value (min/max) → Maybe greedy
├─ Path/sequence → Maybe DP/backtracking
├─ Paired elements → Maybe two pointers
└─ Contiguous subarray → Maybe sliding window

Q4: Problem involves searching?
├─ Sorted array → Binary search
├─ Unsorted → Hash map or linear search
└─ Tree/graph → BFS/DFS

Q5: Can you break into subproblems?
├─ YES, overlapping → DP
├─ YES, non-overlapping → Divide & conquer
└─ NO → Likely greedy or ad-hoc
```

---

# TWO POINTERS PATTERN

## When to Use Two Pointers

**Characteristics:**
- Array or linked list
- Need to find pair/triple/etc meeting condition
- Often can sort first (if allowed)
- Goal: Reduce O(n²) to O(n)

---

## Template: Two Pointers Converging

```python
def two_pointers(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return None

# Complexity:
# Time: O(n) - each pointer moves n steps maximum
# Space: O(1) - only pointers
```

---

## Example 1: Two Sum II - Sorted Array

**Problem:** Find two numbers that add to target in sorted array

```python
def two_sum_sorted(arr, target):
    """
    Input: [2, 3, 5, 8, 11], target=13
    Output: (2, 11)
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

# Trace: [2, 3, 5, 8, 11], target=13
# left=0 (2), right=4 (11): sum=13 ✓ FOUND
```

---

## Example 2: Three Sum

**Problem:** Find all unique triplets that sum to target

```python
def three_sum(arr, target=0):
    """
    Time: O(n²) - sorted + two pointers for each element
    Space: O(1) - excluding output
    """
    arr.sort()  # O(n log n)
    result = []
    
    for i in range(len(arr) - 2):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        # Two-sum on remaining array
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total == target:
                result.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result

# Example: [-1, 0, 1, 2, -1, -4], target=0
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

## Example 3: Valid Palindrome

**Problem:** Check if string is palindrome (ignoring non-alphanumeric)

```python
def is_palindrome(s):
    """
    Time: O(n) - two pointers converge
    Space: O(1) - no extra space
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Example: "A man, a plan, a canal: Panama"
# Output: True
```

---

# SLIDING WINDOW PATTERN

## When to Use Sliding Window

**Characteristics:**
- Problem asks for substring/subarray
- "Longest", "shortest", "contains k", "sum equals"
- Contiguous elements
- Monotonic condition (can slide window)

---

## Template: Sliding Window

```python
def sliding_window(s, pattern):
    """Generic sliding window template"""
    left = 0
    window = {}
    required = {}  # Characters needed
    
    # Build required map
    for char in pattern:
        required[char] = required.get(char, 0) + 1
    
    for right in range(len(s)):
        # Expand: add right character to window
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        # Contract: shrink from left while condition met
        while len(window) == len(required) and \
              all(window.get(c, 0) >= required[c] for c in required):
            # Process current window
            
            # Remove left character
            left_char = s[left]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            left += 1

# Key insight: Expand right, shrink left
# Instead of O(n²), achieve O(n)!
```

---

## Example 1: Longest Substring Without Repeating Characters

**Problem:** Find length of longest substring without duplicate characters

```python
def longest_substring(s):
    """
    Time: O(n) - each character visited twice max
    Space: O(min(n, alphabet_size))
    """
    char_index = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        
        # If char seen and in current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Move left past duplicate
        
        char_index[char] = right  # Update position
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example: "abcabcbb"
# 'a' at 0, 'b' at 1, 'c' at 2
# 'a' again at 3: move left to 1
# "bca" = length 3
# Final: "cab" = length 3
```

---

## Example 2: Minimum Window Substring

**Problem:** Find smallest window containing all characters from pattern

```python
def min_window(s, t):
    """
    Find minimum window substring of s containing all chars in t
    
    Time: O(|s| + |t|) - each char visited twice max
    Space: O(|t|)
    """
    if len(t) > len(s):
        return ""
    
    required = {}
    for char in t:
        required[char] = required.get(char, 0) + 1
    
    left = 0
    formed = 0  # Number of unique chars in window with desired freq
    window = {}
    ans = float('inf'), None, None  # (length, left, right)
    
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        if char in required and window[char] == required[char]:
            formed += 1
        
        # Try shrinking window
        while left <= right and formed == len(required):
            char = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window[char] -= 1
            if char in required and window[char] < required[char]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

# Example: s="ADOBECODEBANC", t="ABC"
# Output: "BANC"
```

---

# BINARY SEARCH PATTERN

## When to Use Binary Search

**Characteristics:**
- Array is SORTED (or can be viewed as sorted)
- Need to find specific element or boundary
- O(log n) required

---

## Template: Binary Search

```python
def binary_search(arr, target):
    """Standard binary search"""
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

---

## Example 1: First Position of Target

**Problem:** Find first occurrence of target in sorted array

```python
def first_position(arr, target):
    """
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Example: [5, 7, 7, 8, 8, 10], target=8
# Output: 3 (first 8)
```

---

## Example 2: Search in Rotated Array

**Problem:** Search in rotated sorted array

```python
def search_rotated(arr, target):
    """
    Example: [4,5,6,7,0,1,2], target=0
    Output: 4
    
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which side is sorted
        if arr[left] <= arr[mid]:  # Left side sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target in left
            else:
                left = mid + 1   # Target in right
        else:  # Right side sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Target in right
            else:
                right = mid - 1  # Target in left
    
    return -1
```

---

# DYNAMIC PROGRAMMING PATTERN

## When to Use DP

**Characteristics:**
- Problem has optimal substructure
- Overlapping subproblems
- Can memoize or tabulate results
- Recurrence relation exists

---

## DP Approach Template

```python
# Step 1: Define state
# dp[i] = answer for problem of size i

# Step 2: Define recurrence
# dp[i] = f(dp[i-1], dp[i-2], ...)

# Step 3: Base cases
# dp[0] = ..., dp[1] = ...

# Step 4: Compute in order
def solve_dp(n):
    dp = [0] * (n + 1)
    dp[0] = base_case_0
    dp[1] = base_case_1
    
    for i in range(2, n + 1):
        dp[i] = f(dp[i-1], dp[i-2], ...)
    
    return dp[n]
```

---

## Example 1: Fibonacci

**Problem:** Find n-th Fibonacci number

```python
def fibonacci(n):
    """
    Recurrence: fib(n) = fib(n-1) + fib(n-2)
    Base: fib(0) = 0, fib(1) = 1
    
    Time: O(n)
    Space: O(n)
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Optimized: O(1) space
def fibonacci_optimized(n):
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr
```

---

## Example 2: Coin Change

**Problem:** Find minimum coins needed for amount

```python
def coin_change(coins, amount):
    """
    Recurrence: dp[i] = min(dp[i - coin] + 1) for all coins
    Base: dp[0] = 0, dp[i] = infinity initially
    
    Time: O(amount × len(coins))
    Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example: coins=[1,2,5], amount=5
# dp[0] = 0
# dp[1] = 1 (one 1-coin)
# dp[2] = 1 (one 2-coin)
# dp[3] = 2 (one 2-coin + one 1-coin)
# dp[4] = 2 (two 2-coins)
# dp[5] = 1 (one 5-coin)
# Output: 1
```

---

## Example 3: Longest Increasing Subsequence

**Problem:** Find length of longest increasing subsequence

```python
def lis(arr):
    """
    Recurrence: dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]
    Base: dp[i] = 1 (each element is LIS of length 1)
    
    Time: O(n²)
    Space: O(n)
    """
    n = len(arr)
    if n == 0:
        return 0
    
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example: [10, 9, 2, 5, 3, 7, 101, 18]
# LIS: [2, 3, 7, 101] or [2, 3, 7, 18]
# Output: 4
```

---

# BACKTRACKING PATTERN

## When to Use Backtracking

**Characteristics:**
- Need to explore all possibilities
- Build solutions incrementally
- Prune branches that can't lead to solution
- Return to previous state when needed

---

## Template: Backtracking

```python
def backtrack(candidates, path, result):
    # Base case: found solution
    if is_solution(path):
        result.append(path[:])  # Add copy
        return
    
    # Choose candidates
    for candidate in candidates:
        if is_valid(candidate, path):
            path.append(candidate)  # Choose
            backtrack(remaining_candidates, path, result)  # Explore
            path.pop()  # Unchoose (backtrack)

# Key: Choose → Explore → Unchoose
```

---

## Example 1: Permutations

**Problem:** Generate all permutations of array

```python
def permutations(nums):
    """
    Generate all permutations of nums
    
    Time: O(n! × n)
    Space: O(n!)
    """
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        
        for i in range(len(remaining)):
            # Choose
            new_remaining = remaining[:i] + remaining[i+1:]
            # Explore
            backtrack(path + [remaining[i]], new_remaining)
            # Implicit unchoose (new_remaining not modified)
    
    backtrack([], nums)
    return result

# Example: [1, 2, 3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

---

## Example 2: Combinations

**Problem:** Find all combinations of k elements

```python
def combinations(n, k):
    """
    Find all combinations of k elements from 1 to n
    
    Time: O(C(n,k) × k)
    Space: O(C(n,k))
    """
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)  # Choose
            backtrack(i + 1, path)  # Explore
            path.pop()  # Unchoose
    
    backtrack(1, [])
    return result

# Example: n=4, k=2
# Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```

---

## Example 3: N-Queens

**Problem:** Place n queens on n×n board, no two attack

```python
def n_queens(n):
    """
    Solve N-Queens problem
    
    Time: O(n!)
    Space: O(n!)
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    
    def is_safe(row, col):
        return col not in cols and \
               row - col not in diag1 and \
               row + col not in diag2
    
    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                # Choose
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Explore
                backtrack(row + 1)
                
                # Unchoose
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
    
    backtrack(0)
    return result
```

---

# BFS/DFS PATTERN

## When to Use BFS/DFS

**Characteristics:**
- Tree or graph traversal
- Need to visit all nodes
- Shortest path (BFS)
- Connected components (DFS)

---

## BFS Template

```python
from collections import deque

def bfs(root):
    """
    Level-order traversal
    Time: O(V + E)
    Space: O(V)
    """
    if not root:
        return
    
    queue = deque([root])
    visited = {root}
    
    while queue:
        node = queue.popleft()
        
        # Process node
        print(node.val)
        
        # Add neighbors
        for neighbor in node.children:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## DFS Template (Recursive)

```python
def dfs(node, visited):
    """
    Depth-first traversal (recursive)
    Time: O(V + E)
    Space: O(V) - recursion stack
    """
    if node in visited:
        return
    
    visited.add(node)
    print(node.val)
    
    for neighbor in node.children:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

---

## DFS Template (Iterative)

```python
def dfs_iterative(root):
    """
    Depth-first traversal (iterative with stack)
    Time: O(V + E)
    Space: O(V)
    """
    if not root:
        return
    
    stack = [root]
    visited = {root}
    
    while stack:
        node = stack.pop()
        print(node.val)
        
        for neighbor in reversed(node.children):  # reversed for order
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```

---

## Example 1: Number of Islands

**Problem:** Count connected components in grid

```python
def num_islands(grid):
    """
    Time: O(m × n)
    Space: O(m × n)
    """
    if not grid:
        return 0
    
    count = 0
    visited = set()
    
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or \
           (r, c) in visited or grid[r][c] == '0':
            return
        
        visited.add((r, c))
        
        # Explore 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1' and (r, c) not in visited:
                count += 1
                dfs(r, c)
    
    return count

# Example: 
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# Output: 3 islands
```

---

# GREEDY PATTERN

## When to Use Greedy

**Characteristics:**
- Make locally optimal choice at each step
- Hope it leads to global optimum
- Can't change previous choices
- Problem has "greedy choice property"

---

## Example 1: Activity Selection

**Problem:** Select maximum non-overlapping activities

```python
def max_activities(activities):
    """
    activities = [(start, end), ...]
    Greedy: Always pick activity that ends earliest
    
    Time: O(n log n) - sorting
    Space: O(1)
    """
    if not activities:
        return []
    
    activities.sort(key=lambda x: x[1])  # Sort by end time
    
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:  # No overlap
            selected.append((start, end))
            last_end = end
    
    return selected

# Example: [(1,3), (2,5), (4,6), (5,7)]
# Sorted by end: [(1,3), (2,5), (4,6), (5,7)]
# Select (1,3) - ends earliest
# Select (4,6) - starts after (1,3) ends
# Output: [(1,3), (4,6)]
```

---

## Example 2: Interval Scheduling

**Problem:** Find minimum number of platforms needed

```python
def min_platforms(arrivals, departures):
    """
    Greedy: Track concurrent arrivals/departures
    
    Time: O(n log n)
    Space: O(1)
    """
    arrivals.sort()
    departures.sort()
    
    platforms = 0
    max_platforms = 0
    i = j = 0
    
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] < departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    return max_platforms

# Example: arrivals=[1,2,3], departures=[3,2,4]
# Events: (1,arrive), (2,arrive), (2,depart), (3,arrive), (3,depart), (4,depart)
# Timeline: 1(+1), 2(+1,−1), 3(+1), 4(−1)
# Max needed: 2
```

---

# SORTING PATTERNS

## Sorting as a Tool

```python
# Problem: Group anagrams
def group_anagrams(words):
    """
    Insight: Anagrams have same sorted characters
    
    Time: O(n × k log k) - n words, k avg length
    Space: O(n)
    """
    groups = {}
    
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())

# Example: ["eat", "tea", "ate", "bat", "tab"]
# "eat", "tea", "ate" → sorted: "aet"
# "bat", "tab" → sorted: "abt"
# Output: [["eat", "tea", "ate"], ["bat", "tab"]]
```

---

# PATTERN DECISION TREE

## Which Pattern to Use?

```
Problem type?

Find pair/multiple elements:
├─ Sum equals target? → Two pointers (if sorted)
├─ Pair exists? → Hash map (check complement)
└─ Combinations? → Backtracking

Find substring/subarray:
├─ Longest/shortest? → Sliding window
├─ Contains pattern? → Sliding window
└─ Sum equals? → Prefix sum / sliding window

Search problem:
├─ Sorted? → Binary search
├─ Unsorted? → Hash map or linear search
└─ In tree/graph? → BFS/DFS

Optimization problem:
├─ Overlapping subproblems? → DP
├─ Greedy choice works? → Greedy
└─ Local search? → Two pointers

Path/sequence problem:
├─ All possibilities? → Backtracking
├─ Shortest path? → BFS
├─ All paths? → DFS
└─ Optimal path? → DP

Arrangement problem:
├─ Permutations? → Backtracking
├─ Combinations? → Backtracking
├─ Sorted order? → Sorting
└─ By category? → Sorting
```

---

# WORKED EXAMPLES

## Example 1: Container With Most Water

```python
def max_area(height):
    """
    Find two lines that form container with max area
    Area = width × min(height)
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)
        
        # Move pointer with smaller height (might find taller)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example: [1,8,6,2,5,4,8,3,7]
# Best: indices 1,8 → width=7, height=min(8,7)=7 → area=49
```

---

## Example 2: Longest Repeating Character Replacement

```python
def character_replacement(s, k):
    """
    Find longest substring after replacing ≤k characters
    
    Time: O(n)
    Space: O(26) = O(1)
    """
    char_count = {}
    left = 0
    max_freq = 0
    max_length = 0
    
    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        max_freq = max(max_freq, char_count[char])
        
        # Window size - max frequency = chars to replace
        if right - left + 1 - max_freq > k:
            left_char = s[left]
            char_count[left_char] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example: s="ABAB", k=2
# Replace 2 B's with A → "AAAA" → length 4
```

---

# INTERVIEW PREPARATION

## Pattern Cheat Sheet

| Pattern | Best For | Example | Complexity |
|---------|----------|---------|------------|
| Two Pointers | Pairs in sorted array | Two Sum | O(n) |
| Sliding Window | Substring problems | Longest substring | O(n) |
| Binary Search | Sorted array search | Find target | O(log n) |
| DP | Optimization | Coin change | O(nk) |
| Backtracking | All solutions | Permutations | O(n!) |
| BFS/DFS | Graph traversal | Islands | O(V+E) |
| Greedy | Optimization | Activity selection | O(n) |
| Sorting | Arrangement | Group anagrams | O(n log n) |

---

**Master these 8 patterns. They solve 70% of all coding problems.** 🎯

