# Phase 13 - Advanced Algorithms (Master Guide)

**Expert-level algorithms for hard problems.**

---

## Divide & Conquer

### Merge Sort (Advanced)

```python
def merge_sort(arr):
    """
    Time: O(n log n)
    Space: O(n)
    Stable: Yes
    """
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

---

### Quick Sort (Advanced with Hoare Partition)

```python
def quick_sort(arr):
    """
    Time: O(n log n) avg, O(n²) worst
    Space: O(log n)
    """
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            sort_helper(low, pi - 1)
            sort_helper(pi + 1, high)
    
    sort_helper(0, len(arr) - 1)
    return arr
```

---

## String Algorithms

### KMP (Knuth-Morris-Pratt)

```python
def build_failure_function(pattern):
    """Build KMP failure function"""
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

def kmp_search(text, pattern):
    """
    Search for pattern in text
    Time: O(n + m)
    Space: O(m)
    """
    n = len(text)
    m = len(pattern)
    failure = build_failure_function(pattern)
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:
            return i - m + 1  # Found at position
    
    return -1
```

---

### Rabin-Karp (Rolling Hash)

```python
def rabin_karp(text, pattern):
    """
    Pattern search using rolling hash
    Time: O(n + m) avg, O(nm) worst
    """
    n, m = len(text), len(pattern)
    prime = 101
    base = 256
    
    pattern_hash = 0
    text_hash = 0
    hash_multiplier = pow(base, m - 1, prime)
    
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i
        
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * hash_multiplier) +
                        ord(text[i + m])) % prime
    
    return -1
```

---

## Matrix Algorithms

### Strassen's Matrix Multiplication

```python
def strassen(A, B):
    """
    Faster matrix multiplication
    Time: O(n^2.807) vs O(n³)
    """
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    
    # Partition matrices
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    # Compute 7 products
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))
    
    # Combine results
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)
    
    # Merge
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    
    return C
```

---

## Optimization Techniques

### Dynamic Programming - Knapsack 0/1

```python
def knapsack_01(capacity, weights, values):
    """
    0/1 Knapsack problem
    Time: O(nW)
    Space: O(nW)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Trace back items selected
def get_items(capacity, weights, values):
    n = len(weights)
    dp = knapsack_01(capacity, weights, values)
    
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]
    
    return items
```

---

### Longest Common Subsequence

```python
def lcs(text1, text2):
    """
    Find LCS length
    Time: O(mn)
    Space: O(mn)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def get_lcs(text1, text2):
    """Reconstruct actual LCS"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack
    lcs_str = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs_str.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs_str))
```

---

## Advanced Searching

### Binary Search - Variations

```python
def first_occurrence(arr, target):
    """Find first position of target"""
    left, right = 0, len(arr) - 1
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

def last_occurrence(arr, target):
    """Find last position of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_rotated(arr, target):
    """Search in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[left] <= arr[mid]:  # Left half sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

## Probabilistic Algorithms

### Miller-Rabin Primality Test

```python
def is_prime(n, k=5):
    """
    Probabilistic primality test
    Error probability: 4^(-k)
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True
```

---

## Competitive Programming Techniques

### Fast I/O

```python
import sys

def fast_input():
    """Fast input for competitive programming"""
    input = sys.stdin.readline
    return input().strip()

# Usage:
n = int(fast_input())
arr = list(map(int, fast_input().split()))
```

---

### Meet in the Middle

```python
def meet_in_middle(arr, target):
    """
    Reduces O(2^n) to O(2^(n/2))
    """
    n = len(arr)
    mid = n // 2
    
    # Generate all sums of first half
    first_half_sums = {}
    for mask in range(1 << mid):
        s = 0
        for i in range(mid):
            if mask & (1 << i):
                s += arr[i]
        
        if s not in first_half_sums:
            first_half_sums[s] = []
        first_half_sums[s].append(mask)
    
    # Check second half against first
    count = 0
    for mask in range(1 << (n - mid)):
        s = 0
        for i in range(n - mid):
            if mask & (1 << i):
                s += arr[mid + i]
        
        need = target - s
        if need in first_half_sums:
            count += len(first_half_sums[need])
    
    return count
```

---

**Master advanced algorithms for expert-level problem solving.** 🎯

