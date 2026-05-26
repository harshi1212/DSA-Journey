# 🧩 Problem Variant Guide

**"I solved problem X. How do I solve similar problems?"**

Learn to adapt your solution to 5+ variations. This separates good from great.

---

## Core Pattern: Two Sum

### Variant 1: Two Sum - Original
```
Problem: Given array, find two numbers that sum to target
Example: [2, 7, 11, 15], target=9 -> [0, 1] (2+7=9)
```

**Solution: Hash Map O(n)**
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

---

### Variant 2: Two Sum II - Sorted Array
```
Problem: Array is SORTED, find two numbers that sum to target
Example: [2, 7, 11, 15], target=9 -> [1, 2]
Note: Can't use hash map efficiently, must use sorted property!
```

**Solution: Two Pointers O(n)**
```python
def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left + 1, right + 1]  # 1-indexed
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

**Key adaptation:** Sorted array → Use two pointers instead of hash map.

---

### Variant 3: Three Sum
```
Problem: Find ALL unique triplets that sum to target
Example: [-1, 0, 1, 2, -1, -4], target=0
Result: [[-1, -1, 2], [-1, 0, 1]]
```

**Solution: Sort + Two Pointers O(n²)**
```python
def threeSum(nums, target=0):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Two sum on remaining
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    
    return result
```

**Key adaptation:** Multiple numbers → Reduce to two sum at each step.

---

### Variant 4: Four Sum
```
Problem: Find ALL unique quadruplets that sum to target
Example: [1000000000, 1000000000, 1000000000, 1000000000], target=-294967296
Result: []
Note: Watch for integer overflow!
```

**Solution: Sort + Nested Two Sum O(n³)**
```python
def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            # Two sum for remaining
            left, right = j + 1, n - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    
    return result
```

**Key adaptation:** K sum problem → Reduce to (K-1) sum recursively.

---

### Variant 5: Two Sum - Closest
```
Problem: Find two numbers whose sum is CLOSEST to target (not exact)
Example: [-1, 2, 1, -4], target=1 -> [1, 1] (sum=2, closest to 1)
```

**Solution: Two Pointers O(n log n)**
```python
def twoSumClosest(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    closest_sum = float('inf')
    best_pair = []
    
    while left < right:
        s = nums[left] + nums[right]
        
        # Update if this sum is closer
        if abs(s - target) < abs(closest_sum - target):
            closest_sum = s
            best_pair = [nums[left], nums[right]]
        
        # Move pointers
        if s < target:
            left += 1
        else:
            right -= 1
    
    return best_pair
```

**Key adaptation:** Instead of finding exact match, track closest difference.

---

### Variant 6: Two Sum - Count Pairs
```
Problem: Count how MANY pairs sum to target (not return pairs)
Example: [1, 1, 1, 2, 2], target=3 -> 3 pairs: (1,2), (1,2), (1,2)
```

**Solution: Hash Map O(n)**
```python
def countTwoPairSum(nums, target):
    counter = {}
    result = 0
    
    for num in nums:
        complement = target - num
        if complement in counter:
            result += counter[complement]
        
        counter[num] = counter.get(num, 0) + 1
    
    return result
```

**Key adaptation:** Count occurrences, multiply counts instead of storing pairs.

---

## Pattern: Sliding Window

### Base: Longest Substring Without Repeating
```python
def lengthOfLongestSubstring(s):
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### Variant 1: Longest Substring with At Most K Distinct Chars
```python
def lengthOfLongestSubstringKDistinct(s, k):
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window if too many distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

**Key adaptation:** Track count instead of just membership.

---

### Variant 2: Longest Subarray with Sum = K
```python
def longestSubarrayWithSumK(arr, k):
    sum_map = {0: -1}  # prefix_sum -> earliest index
    max_len = 0
    current_sum = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # If (current_sum - k) exists, subarray between exists
        if current_sum - k in sum_map:
            max_len = max(max_len, i - sum_map[current_sum - k])
        
        # Store first occurrence of this sum
        if current_sum not in sum_map:
            sum_map[current_sum] = i
    
    return max_len
```

**Key adaptation:** Use prefix sum + hash map instead of window.

---

## Pattern: Binary Search

### Base: Find Target
```python
def binarySearch(arr, target):
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

### Variant 1: Find First Occurrence
```python
def findFirst(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

**Key adaptation:** When found, don't return immediately - keep searching.

---

### Variant 2: Find Minimum in Rotated Array
```python
def findMin(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If middle is greater than right, min is on right
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]
```

**Key adaptation:** Compare middle with boundary, not target.

---

## Pattern: DP

### Base: House Robber (1D)
```python
def rob(nums):
    if not nums:
        return 0
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    
    return dp[len(nums)]
```

### Variant 1: House Robber II (Circular)
```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Can't rob first and last together
    return max(
        rob_linear(nums[:-1]),  # Rob except last
        rob_linear(nums[1:])    # Rob except first
    )

def rob_linear(nums):
    if not nums:
        return 0
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    
    return dp[len(nums)]
```

**Key adaptation:** Circular constraint → Split into two linear problems.

---

### Variant 2: House Robber III (Tree)
```python
def rob(root):
    def dfs(node):
        if not node:
            return [0, 0]  # [rob_this, rob_children]
        
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        
        # Rob this house: can't rob children
        rob_this = node.val + left_skip + right_skip
        
        # Skip this house: can rob or skip children
        skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
        
        return [rob_this, skip_this]
    
    rob_val, skip_val = dfs(root)
    return max(rob_val, skip_val)
```

**Key adaptation:** Tree DP returns two states: rob or skip.

---

## Adaptation Pattern Recognition

| Adaptation | Trigger | Solution |
|-----------|---------|----------|
| Multiple numbers → One number | K-sum | Reduce to (K-1) sum |
| Array sorted | Given constraint | Use two pointers |
| Circular constraint | Adjacent can't both | Split into two linear |
| Tree instead of array | Structure change | Use DFS, return multiple states |
| Count instead of find | Different question | Track counts, not pairs |
| Closest instead of exact | Modified goal | Track best diff, not match |
| At most K instead of exactly | Generalization | Change boundary condition |

---

## 🎯 Adaptation Strategy

When facing new variant:

1. **Identify base pattern** - Is this Two Sum, DP, Sliding Window?
2. **Identify constraint change** - What's different from base?
3. **Map to table above** - What's the adaptation?
4. **Apply transformation** - Modify base solution
5. **Test carefully** - Edge cases specific to variant

---

**Master these variants. Then face any similar problem with confidence!** 💪

