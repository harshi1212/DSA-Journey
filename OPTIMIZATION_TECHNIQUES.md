# Optimization Techniques Guide

## How to Improve from Brute Force to Optimal

This guide teaches you **patterns for optimization** so you can convert slow solutions to fast ones.

---

## **The Optimization Spectrum**

```
Brute Force O(n²)
    ↓
Add Hash Map O(n)
    ↓
Use Two Pointers O(n)
    ↓
Binary Search O(log n)
    ↓
Dynamic Programming O(n)
    ↓
Advanced Algorithm O(n log n)
```

Learn these progression patterns!

---

## **PATTERN 1: Brute Force → Hash Map**

**When**: Checking existence, counting frequency, finding pairs

### Example: Two Sum

**Problem**: Given array, find two numbers that sum to target

**Brute Force** O(n²):
```python
def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []
```

**Optimization**: Use hash map to track seen numbers
```python
def twoSum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Result**: O(n²) → O(n) ✓

---

### Example: Duplicate Check

**Brute Force** O(n²):
```python
def hasDuplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

**Optimization**: Use set
```python
def hasDuplicate(arr):
    return len(arr) != len(set(arr))
```

**Result**: O(n²) → O(n) ✓

---

### Pattern Summary

| Problem | Brute Force | Optimization |
|---------|-------------|--------------|
| Find pair | O(n²) nested | O(n) hash map |
| Count frequency | O(n²) lookup | O(n) hash map |
| Find duplicate | O(n²) nested | O(n) set |
| Find target | O(n²) nested | O(n) hash map |

**Template**:
```python
# Instead of checking all pairs:
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if condition(arr[i], arr[j]):
            ...

# Use hash map:
seen = {}
for num in arr:
    if (target - num) in seen:
        return seen[target - num]
    seen[num] = ...
```

---

## **PATTERN 2: Brute Force → Two Pointers**

**When**: Sorted array, need to check pairs from both ends

### Example: Container With Most Water

**Brute Force** O(n²):
```python
def maxArea(heights):
    max_area = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, area)
    return max_area
```

**Key Insight**: If you have two lines, moving the shorter one inward can only decrease area (because width decreases). So skip it!

**Optimization**: Two pointers from both ends
```python
def maxArea(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)
        
        # Move the shorter line inward
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

**Result**: O(n²) → O(n) ✓

---

### Example: Valid Palindrome

**Brute Force** O(n):
```python
def validPalindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]  # O(n) for reversal
```

**Optimization**: Two pointers
```python
def validPalindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

**Result**: O(n) with extra space → O(n) with O(1) space ✓

---

### Pattern Summary

| Problem | Brute Force | Optimization |
|---------|-------------|--------------|
| Container | O(n²) nested | O(n) two pointers |
| Palindrome check | O(n) with reversal | O(n) with O(1) space |
| Sorted array pairs | O(n²) nested | O(n) two pointers |

**Template**:
```python
left, right = 0, len(arr) - 1

while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

---

## **PATTERN 3: Multiple Pass → Sliding Window**

**When**: Substring/subarray problems, continuous range

### Example: Longest Substring Without Repeating

**Brute Force** O(n²):
```python
def lengthOfLongestSubstring(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            if len(set(s[i:j])) == j - i:  # All unique
                max_len = max(max_len, j - i)
    return max_len
```

**Optimization**: Sliding window with hash map
```python
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in seen:
            # Move left to skip duplicate
            left = max(left, seen[s[right]] + 1)
        
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

**Result**: O(n²) → O(n) ✓

---

### Example: Maximum Subarray

**Brute Force** O(n²):
```python
def maxSubArray(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum
```

**Optimization**: Kadane's algorithm (variant of DP)
```python
def maxSubArray(arr):
    max_sum = current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**Result**: O(n²) → O(n) ✓

---

### Pattern Summary

| Problem | Brute Force | Optimization |
|---------|-------------|--------------|
| Longest substring | O(n²) nested | O(n) sliding window |
| Subarray sum | O(n²) nested | O(n) Kadane |
| Min window | O(n²) nested | O(n) sliding window |

**Template**:
```python
window = {}
left = 0
result = 0

for right in range(len(arr)):
    # Add to window
    window[arr[right]] = ...
    
    # Shrink window if needed
    while condition_met:
        left += 1
    
    # Update result
    result = max(result, right - left + 1)
```

---

## **PATTERN 4: Linear Search → Binary Search**

**When**: Sorted data, decision problem

### Example: Find Target

**Brute Force** O(n):
```python
def search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False
```

**Optimization**: Binary search
```python
def search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
```

**Result**: O(n) → O(log n) ✓

---

### Example: Find First Position

**Brute Force** O(n):
```python
def findFirst(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1
```

**Optimization**: Binary search with variant
```python
def findFirst(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left if left < len(arr) and arr[left] == target else -1
```

**Result**: O(n) → O(log n) ✓

---

### Pattern Summary

| Problem | Brute Force | Optimization |
|---------|-------------|--------------|
| Find target | O(n) linear | O(log n) binary search |
| Find boundary | O(n) linear | O(log n) binary search variant |
| Find in rotated | O(n) linear | O(log n) modified binary search |

**Template**:
```python
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

## **PATTERN 5: Recursion → Dynamic Programming**

**When**: Overlapping subproblems, optimal substructure

### Example: Fibonacci

**Brute Force Recursion** O(2^n):
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # Recalculates many times!
```

**Optimization 1: Memoization** O(n):
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

**Optimization 2: Tabulation** O(n):
```python
def fib(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

**Result**: O(2^n) → O(n) ✓

---

### Example: Climbing Stairs

**Brute Force Recursion** O(2^n):
```python
def climbStairs(n):
    if n <= 1:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)
```

**Optimization: DP** O(n):
```python
def climbStairs(n):
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

**Result**: O(2^n) → O(n) ✓

---

### Pattern Summary

| Problem | Brute Force | Optimization |
|---------|-------------|--------------|
| Fibonacci | O(2^n) recursion | O(n) memoization |
| Climbing stairs | O(2^n) recursion | O(n) DP |
| Coin change | O(n^m) recursion | O(n*m) DP |

**Template**:
```python
# Define state
dp = [0] * (n + 1)

# Base case
dp[0] = base_value

# Recurrence
for i in range(1, n + 1):
    dp[i] = function_of(dp[i-1], dp[i-2], ...)

return dp[n]
```

---

## **PATTERN 6: Nested Loops → Sorting + Two Pointers**

**When**: Need to find pairs but can sort first

### Example: 3Sum

**Brute Force** O(n³):
```python
def threeSum(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    result.append([arr[i], arr[j], arr[k]])
    return result
```

**Optimization**: Sort + two pointers
```python
def threeSum(arr, target):
    arr.sort()  # O(n log n)
    result = []
    
    for i in range(len(arr) - 2):
        # Two sum problem with two pointers
        left, right = i + 1, len(arr) - 1
        
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result
```

**Result**: O(n³) → O(n²) ✓

---

### Pattern Summary

**Key Insight**: Sorting is O(n log n), but if it enables O(n) solution, total is O(n log n)!

| Problem | Brute Force | Optimization |
|---------|-------------|--------------|
| 3Sum | O(n³) | O(n²) sort + two pointers |
| 4Sum | O(n⁴) | O(n³) sort + two pointers |
| Merge intervals | O(n²) | O(n log n) sort + merge |

**Template**:
```python
arr.sort()

for i in range(len(arr)):
    left, right = i + 1, len(arr) - 1
    
    while left < right:
        total = arr[i] + arr[left] + arr[right]
        
        if total == target:
            result.append([...])
        # Move pointers
```

---

## **PATTERN 7: Multiple Algorithms → Advanced Algorithm**

**When**: Basic algorithms can't achieve target complexity

### Example: Shortest Path in Unweighted Graph

**Brute Force** O(n!):
```python
# Try all paths - exponential!
def shortestPath(graph, start, end):
    # DFS trying all paths
    pass
```

**Optimization**: BFS (designed for unweighted)
```python
from collections import deque

def shortestPath(graph, start, end):
    queue = deque([start])
    visited = {start}
    distance = {start: 0}
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            return distance[end]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    return -1
```

**Result**: O(n!) → O(V + E) ✓

---

### Example: Shortest Path in Weighted Graph

**Algorithm**: Dijkstra
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        
        if current_dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances
```

**Result**: O(V²) naive → O((V + E) log V) Dijkstra ✓

---

## **Optimization Decision Tree**

```
Problem seems slow?
├─ Are you checking all pairs? (O(n²))
│  ├─ Can you use a hash map? → Use hash map O(n) ✓
│  └─ Is data sorted? → Use two pointers O(n) ✓
│
├─ Doing substring/subarray checks? (O(n²))
│  └─ Use sliding window O(n) ✓
│
├─ Searching sorted array?
│  └─ Use binary search O(log n) ✓
│
├─ Recursive with overlapping subproblems? (O(2^n))
│  └─ Use memoization/DP O(n) ✓
│
├─ Graph problem?
│  ├─ Unweighted shortest path? → BFS O(V+E) ✓
│  ├─ Weighted shortest path? → Dijkstra O((V+E)logV) ✓
│  └─ Need all pairs? → Floyd-Warshall O(V³) ✓
│
└─ Still slow?
   └─ Need advanced algorithm (segment tree, etc.)
```

---

## **Optimization Checklist**

Before submitting, ask:

- [ ] Can I use a hash map to avoid nested loops?
- [ ] Can I sort first and use two pointers?
- [ ] Can I use sliding window instead of nested loops?
- [ ] Is binary search applicable?
- [ ] Are there overlapping subproblems (DP)?
- [ ] Should I use a different data structure?
- [ ] Is there a specialized algorithm for this?

**Time saved**: 30% of optimization happens with these 7 patterns!

---

## **Practice Problems by Optimization Type**

### Hash Map Optimization
- Two Sum (1)
- Contains Duplicate (217)
- Valid Anagram (242)
- Majority Element (169)

### Two Pointers Optimization
- Container With Most Water (11)
- 3Sum (15)
- Valid Palindrome (125)
- Merge Sorted Array (88)

### Sliding Window Optimization
- Longest Substring Without Repeating (3)
- Minimum Window Substring (76)
- Sliding Window Maximum (239)

### Binary Search Optimization
- Search in Rotated Array (33)
- Find First and Last Position (34)
- Median of Two Sorted Arrays (4)

### DP Optimization
- Climbing Stairs (70)
- Coin Change (322)
- Edit Distance (72)
- Longest Increasing Subsequence (300)

---

## **Pro Tips**

1. **Optimization starts during design** - Think about it before coding
2. **Discuss with interviewer** - "Can I optimize this? What if I use a hash map?"
3. **Trade-off space for time** - Use hash map/extra space to reduce time
4. **Verify with manual trace** - Confirm optimized solution works
5. **Common patterns** - Learn the 7 patterns deeply

---

**Master these patterns = 80% of interview optimization questions!** 🎯
