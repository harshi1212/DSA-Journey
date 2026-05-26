# ⚠️ Common Beginner Mistakes & How to Avoid Them

**The 40 mistakes we all make. Learn them. Never make them again.**

---

## 🔴 PHASE 0-2: Setup & Python Basics

### Mistake 1: Assuming Python version differences don't matter
**❌ Wrong:**
```python
# Python 2 vs 3 differences cause confusion
print "Hello"  # Works in Python 2, fails in Python 3
```

**✅ Right:**
```python
# Always use Python 3
print("Hello")  # Works everywhere
```

**Impact:** Your code won't run. Major frustration.

---

### Mistake 2: Using mutable default arguments
**❌ Wrong:**
```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2] - WRONG! Expected [2]
```

**✅ Right:**
```python
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**Why it matters:** Default arguments are created once at function definition. They're shared across calls!

---

### Mistake 3: Confusing `==` and `is`
**❌ Wrong:**
```python
if x is None:  # Sometimes works, unreliable
    pass

if x is 5:  # Don't do this! Works sometimes, not always
    pass
```

**✅ Right:**
```python
if x is None:  # Correct for None check
    pass

if x == 5:  # Use == for value comparison
    pass

if isinstance(x, int):  # Use isinstance for type checking
    pass
```

**Why it matters:** `is` checks object identity, not value. Leads to subtle bugs.

---

### Mistake 4: Off-by-one errors in loops
**❌ Wrong:**
```python
n = 5
for i in range(n):  # 0, 1, 2, 3, 4
    print(i)  # Missing 5!
    
# Or trying to access arr[n] when it doesn't exist
```

**✅ Right:**
```python
n = 5
for i in range(n):  # If you need 0-4, this is correct
    print(i)

for i in range(1, n+1):  # If you need 1-5, use this
    print(i)
    
# Always check: Do I need inclusive or exclusive end?
```

**Why it matters:** Most array indexing bugs come from this. Cost: hours of debugging.

---

### Mistake 5: Not understanding list vs array indexing
**❌ Wrong:**
```python
arr = [1, 2, 3, 4, 5]
print(arr[5])  # IndexError! Only 0-4 valid
print(arr[-6])  # IndexError! Only -1 to -5 valid
```

**✅ Right:**
```python
arr = [1, 2, 3, 4, 5]
print(arr[4])  # 5 ✓
print(arr[-1])  # 5 ✓
print(len(arr))  # 5

# Safe access
if 0 <= index < len(arr):
    print(arr[index])
```

**Why it matters:** IndexError crashes your program. Learn Python indexing deeply.

---

## 🔴 PHASE 3-5: Data Structures

### Mistake 6: Mutating during iteration
**❌ Wrong:**
```python
lst = [1, 2, 3, 4, 5]
for item in lst:
    if item % 2 == 0:
        lst.remove(item)  # WRONG! Causes elements to skip
# Result: [1, 3, 5] but you might miss some!
```

**✅ Right:**
```python
lst = [1, 2, 3, 4, 5]

# Option 1: Iterate over copy
for item in lst[:]:  # [:] creates a copy
    if item % 2 == 0:
        lst.remove(item)

# Option 2: List comprehension
lst = [item for item in lst if item % 2 != 0]

# Option 3: Iterate backwards
for i in range(len(lst) - 1, -1, -1):
    if lst[i] % 2 == 0:
        lst.pop(i)
```

**Why it matters:** Skips elements, misses bugs, corrupts data.

---

### Mistake 7: Not copying nested structures
**❌ Wrong:**
```python
matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1  # Shallow copy!

matrix2[0][0] = 99
print(matrix1)  # [[99, 2], [3, 4]] - CHANGED! WRONG!
```

**✅ Right:**
```python
import copy

matrix1 = [[1, 2], [3, 4]]
matrix2 = copy.deepcopy(matrix1)  # Deep copy

matrix2[0][0] = 99
print(matrix1)  # [[1, 2], [3, 4]] - unchanged ✓
```

**Why it matters:** Accidentally modifying original data. Very subtle bugs.

---

### Mistake 8: Hash map key must be hashable
**❌ Wrong:**
```python
hashmap = {}
lst = [1, 2, 3]
hashmap[lst] = "value"  # TypeError! Lists aren't hashable
```

**✅ Right:**
```python
hashmap = {}
tup = (1, 2, 3)
hashmap[tup] = "value"  # Tuples ARE hashable ✓

# For arrays, convert to tuple first
arr = [1, 2, 3]
hashmap[tuple(arr)] = "value"  # Works ✓
```

**Why it matters:** "TypeError: unhashable type" crashes. Use tuples for keys.

---

### Mistake 9: Not understanding hash set vs hash map
**❌ Wrong:**
```python
# When you need to store values
s = set()
s.add((key, value))  # Wrong way!

# When you need uniqueness + associated data
seen = {"key1": [data1, data2], "key2": [data3]}
```

**✅ Right:**
```python
# For storing values with keys
d = {}  # or dict()
d["key"] = "value"

# For just uniqueness
s = set()
s.add(item)

# Check membership
if "key" in d:  # O(1)
    pass

if item in s:  # O(1)
    pass
```

**Why it matters:** Right tool for right job. Performance + clarity.

---

### Mistake 10: Stack vs Queue confusion
**❌ Wrong:**
```python
from collections import deque

# Using list as stack (inefficient)
stack = []
stack.append(1)  # O(1)
stack.pop(0)  # O(n) - WRONG! Slow!

# Using list as queue (inefficient)
queue = []
queue.append(1)  # O(1)
queue.pop(0)  # O(n) - WRONG! Slow!
```

**✅ Right:**
```python
from collections import deque

# Stack - use list (pop from end is O(1))
stack = []
stack.append(1)  # O(1)
stack.pop()  # O(1)

# Queue - use deque (both ends are O(1))
queue = deque()
queue.append(1)  # O(1) - append right
queue.popleft()  # O(1) - pop left
```

**Why it matters:** Performance differs by 10-100x. Learn the right structure.

---

## 🔴 PHASE 6: Algorithms

### Mistake 11: Not handling edge cases for binary search
**❌ Wrong:**
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

# Edge case: empty array
print(binary_search([], 5))  # Should return -1 ✓
# Edge case: single element
print(binary_search([5], 5))  # Should return 0 ✓
# Edge case: target not in array
print(binary_search([1, 3, 5], 2))  # Should return -1 ✓
```

**✅ Right:** (above code is correct, check before submitting!)

**Why it matters:** Binary search is trickier than it looks. Edge cases are critical.

---

### Mistake 12: Recursion without base case
**❌ Wrong:**
```python
def factorial(n):
    return n * factorial(n - 1)  # No base case!
    # RecursionError: maximum recursion depth exceeded
```

**✅ Right:**
```python
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)
```

**Why it matters:** Stack overflow. Always include base case before recursive call.

---

### Mistake 13: Comparing floats with ==
**❌ Wrong:**
```python
x = 0.1 + 0.1 + 0.1
if x == 0.3:
    print("Equal")
else:
    print("Not equal")  # Prints this! Due to floating point precision
```

**✅ Right:**
```python
import math

x = 0.1 + 0.1 + 0.1
epsilon = 1e-9

if abs(x - 0.3) < epsilon:
    print("Equal")
else:
    print("Not equal")

# Or use math.isclose (Python 3.5+)
if math.isclose(x, 0.3):
    print("Equal")
```

**Why it matters:** Floating point precision varies. Always use epsilon comparison.

---

### Mistake 14: Not resetting variables in loops
**❌ Wrong:**
```python
max_val = float('-inf')
for test in test_cases:
    # Process test
    max_in_test = find_max(test)
    max_val = max(max_val, max_in_test)  # Accumulates across tests!

# Output accumulated max across all tests - WRONG!
```

**✅ Right:**
```python
for test in test_cases:
    max_val = float('-inf')  # Reset for each test
    max_in_test = find_max(test)
    max_val = max(max_val, max_in_test)
    
    # Process max_val for this test only
    print(max_val)
```

**Why it matters:** State leaks between iterations. Hard to debug.

---

## 🔴 PHASE 7: Core Patterns

### Mistake 15: Two pointers - not handling duplicates
**❌ Wrong:**
```python
def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if nums[i] + nums[i+1] + nums[i+2] > 0:
            continue  # Doesn't handle duplicates properly!
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
            # Missing: Skip duplicate left/right values!
```

**✅ Right:**
```python
def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate i
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

**Why it matters:** Duplicate results. Edge case handling separates good from great solutions.

---

### Mistake 16: Sliding window - not expanding when possible
**❌ Wrong:**
```python
def maxSlidingWindow(nums, k):
    result = []
    window = deque()
    
    for i in range(len(nums)):
        # Remove element outside window
        if window and window[0] == i - k:
            window.popleft()
        
        # Add current element
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        window.append(i)
        
        # Add to result (missing condition!)
        result.append(nums[window[0]])  # Adds even before window is full!
    
    return result
```

**✅ Right:**
```python
def maxSlidingWindow(nums, k):
    result = []
    window = deque()
    
    for i in range(len(nums)):
        if window and window[0] == i - k:
            window.popleft()
        
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        window.append(i)
        
        # Only add when window is full!
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result
```

**Why it matters:** Wrong results before window size reached.

---

### Mistake 17: DP - not initializing correctly
**❌ Wrong:**
```python
def maxSumSubarray(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1] + arr[i])  # What if dp[i-1] = 0?
    
    return max(dp)  # Could miss maximum if all negative
```

**✅ Right:**
```python
def maxSumSubarray(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]  # Track max separately
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**Why it matters:** Wrong answer when results are negative or edge cases.

---

### Mistake 18: Backtracking - forgetting to backtrack
**❌ Wrong:**
```python
def permute(nums):
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path)  # BUG: path is reference!
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                # FORGOT TO BACKTRACK!
    
    backtrack([])
    return result
```

**✅ Right:**
```python
def permute(nums):
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])  # Copy the path
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()  # BACKTRACK!
    
    backtrack([])
    return result
```

**Why it matters:** Missing backtrack = wrong permutations, duplicates, or crashes.

---

### Mistake 19: BFS/DFS - visiting same node twice
**❌ Wrong:**
```python
def bfs(graph, start):
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print(node)
        
        for neighbor in graph[node]:
            queue.append(neighbor)  # No visited check!
            # If graph has cycle, infinite loop!
```

**✅ Right:**
```python
def bfs(graph, start):
    queue = deque([start])
    visited = {start}  # Track visited nodes
    
    while queue:
        node = queue.popleft()
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Why it matters:** Infinite loops in cyclic graphs. Always track visited.

---

### Mistake 20: DFS - return value confusion
**❌ Wrong:**
```python
def canReach(graph, start, target):
    if start == target:
        return True
    
    for neighbor in graph[start]:
        if canReach(graph, neighbor, target):
            pass  # FORGOT TO RETURN!
    
    return False
```

**✅ Right:**
```python
def canReach(graph, start, target):
    if start == target:
        return True
    
    for neighbor in graph[start]:
        if canReach(graph, neighbor, target):
            return True  # Return immediately!
    
    return False
```

**Why it matters:** Doesn't stop when found. Wrong answer.

---

## 🔴 PHASE 12-13: Graphs

### Mistake 21: Dijkstra - not using priority queue
**❌ Wrong:**
```python
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    for _ in range(len(graph)):
        # Find unvisited node with min distance - O(V)
        u = min(graph, key=lambda x: dist[x] if x in unvisited else float('inf'))
        # ... rest of code
        # Overall: O(V²)  - Too slow for large graphs!
```

**✅ Right:**
```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    pq = [(0, start)]  # Use priority queue
    
    while pq:
        d, u = heapq.heappop(pq)  # O(log V)
        
        if d > dist[u]:  # Already found better path
            continue
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist  # O(E log V) - Much faster!
```

**Why it matters:** 100x slower without priority queue. Time limit exceeded!

---

### Mistake 22: Union-Find - path compression
**❌ Wrong:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
    
# Missing: Rank-based union!
```

**✅ Right:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Add rank
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Rank-based union - attach smaller tree to larger
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True
```

**Why it matters:** Path compression alone is O(α(n)) amortized, but rank makes it consistent.

---

### Mistake 23: Topological sort - not checking all nodes
**❌ Wrong:**
```python
def topologicalSort(graph):
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
        
        result.append(node)
    
    # Only starts from node 0 if graph is sparse!
    dfs(0)
    return result[::-1]
```

**✅ Right:**
```python
def topologicalSort(graph):
    visited = set()
    result = []
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
        
        result.append(node)
    
    # Start from ALL nodes
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return result[::-1]
```

**Why it matters:** Disconnected components. Missing nodes from result.

---

## 🔴 PHASE 14-19: Advanced Topics

### Mistake 24: Greedy without proving it works
**❌ Wrong:**
```python
# Student tries greedy for 0/1 knapsack
def knapsack_greedy(items, capacity):
    # Sort by value/weight ratio
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0
    total_weight = 0
    
    for weight, value in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
    
    return total_value
    # WRONG! Greedy doesn't work for 0/1 knapsack!
```

**✅ Right:**
```python
# Use DP for 0/1 knapsack (greedy doesn't work!)
def knapsack_dp(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

**Why it matters:** Greedy works for SOME problems, not all. Always verify first!

---

### Mistake 25: KMP - not building failure function correctly
**❌ Wrong:**
```python
def kmp_search_wrong(text, pattern):
    # Builds naive failure function - inefficient
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:  # O(nm)
            return i
    return -1
```

**✅ Right:**
```python
def kmp_search(text, pattern):
    # Build proper failure function
    def build_failure_function(pattern):
        m = len(pattern)
        failure = [0] * m
        j = 0
        
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = failure[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            failure[i] = j
        
        return failure
    
    n, m = len(text), len(pattern)
    failure = build_failure_function(pattern)
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    
    return -1
```

**Why it matters:** Naive is O(nm), KMP is O(n+m). Huge difference!

---

## 🎓 Mistake Summary by Severity

### 🔴 Critical (Crash Program)
1. Off-by-one in loops
2. No base case in recursion
3. Mutating list during iteration
4. Visiting same node twice in graph
5. No visited set in BFS/DFS

### 🟠 High (Wrong Answer)
1. Not handling edge cases
2. Forgetting to backtrack
3. Wrong data structure (list vs deque)
4. Not skipping duplicates
5. Greedy without proof

### 🟡 Medium (Inefficient)
1. No priority queue in Dijkstra
2. Naive binary search
3. Floating point comparison
4. String concatenation in loops
5. No path compression in Union-Find

### 🟢 Low (Poor Practice)
1. Poor variable names
2. Missing comments
3. Not testing edge cases
4. Hardcoding values
5. No complexity analysis

---

## ✅ Beginner's Mistake Prevention Checklist

Before submitting code:

- [ ] Did I handle empty input? (empty array, empty string, n=0)
- [ ] Did I handle single element? (n=1)
- [ ] Did I handle negative numbers?
- [ ] Did I handle duplicates?
- [ ] Are my loop indices correct? (off-by-one?)
- [ ] Did I initialize variables before using?
- [ ] Did I reset state between iterations?
- [ ] For recursion: Is there a base case?
- [ ] For graphs: Did I mark nodes as visited?
- [ ] For backtracking: Did I backtrack (undo)?
- [ ] Is my complexity analysis correct?
- [ ] Did I test with provided examples first?
- [ ] Did I test with edge cases?
- [ ] Is my code readable? (good naming, comments)

---

## 🚀 Master This

**Print this. Reference daily. These 25 mistakes account for 80% of beginner bugs.**

Learn the mistake → Never make it again → Interview ready! 💪

