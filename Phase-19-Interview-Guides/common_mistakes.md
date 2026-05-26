# Common Mistakes Encyclopedia

## Top 20 Interview Mistakes

### 1. **Off-by-One Errors** (Most Common)

**Mistake**:
```python
# Forgot to include last element
for i in range(n):  # Should be range(n+1)
    result += arr[i]
```

**How to catch**:
- Print boundary cases
- Trace through manually for n=1, n=2

---

### 2. **Not Handling Edge Cases**

**Mistake**:
```python
def min_val(arr):
    return min(arr)  # Crashes on empty []
```

**Fix**:
```python
def min_val(arr):
    if not arr:
        return None
    return min(arr)
```

---

### 3. **Modifying Input During Iteration**

**Mistake**:
```python
for item in arr:
    if bad(item):
        arr.remove(item)  # Skips next item!
```

**Fix**:
```python
result = [x for x in arr if not bad(x)]
```

---

### 4. **Wrong Time Complexity**

**Mistake**:
```python
def solve(arr):
    for i in arr:
        for j in arr:
            # O(n²) but should be O(n)
            pass
```

**How to catch**:
- Count nested loops
- State O(?) before coding

---

### 5. **Forgetting Base Case in Recursion**

**Mistake**:
```python
def fib(n):
    return fib(n-1) + fib(n-2)  # Infinite recursion!
```

**Fix**:
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

---

### 6. **Integer Overflow**

**Mistake**:
```python
result = a * b  # Overflow if a, b very large
```

**Fix** (in Java/C++):
```python
result = (a % MOD) * (b % MOD) % MOD
```

**Python**: No overflow, but watch performance

---

### 7. **Wrong Variable Reference**

**Mistake**:
```python
class Solution:
    def __init__(self):
        self.count = 0
    
    def solve(self):
        count = 0  # Wrong! Local, not self.count
        count += 1
```

---

### 8. **Comparing Objects Wrong**

**Mistake**:
```python
if node1 == node2:  # Compares references, not values
    pass
```

**Fix**:
```python
if node1.val == node2.val:
    pass
```

---

### 9. **Assuming Input Constraints**

**Mistake**:
```python
# Problem says arr has n elements
# But you assume all positive
# Didn't read: "can be negative"
```

**Fix**: Read constraints 3 times!

---

### 10. **Not Testing Negative Numbers**

**Mistake**:
```python
# Works for [1, 2, 3]
# Breaks for [-3, -1, 0, 2]
# Forgot to test negatives
```

---

### 11. **Mutation During Dict Iteration**

**Mistake**:
```python
for key in dict:
    if condition(key):
        del dict[key]  # RuntimeError!
```

**Fix**:
```python
keys_to_delete = [k for k in dict if condition(k)]
for k in keys_to_delete:
    del dict[k]
```

---

### 12. **Not Resetting State**

**Mistake**:
```python
def solve(arr):
    global_var = 0
    # Previous test's value still in global_var!
```

---

### 13. **Floating Point Precision**

**Mistake**:
```python
if 0.1 + 0.2 == 0.3:  # False! (precision)
    pass
```

**Fix**:
```python
if abs(0.1 + 0.2 - 0.3) < 1e-9:
    pass
```

---

### 14. **Using Set/Dict Wrong**

**Mistake**:
```python
seen = [False] * n
for item in arr:
    if not seen[item]:  # IndexError if item > n!
        seen[item] = True
```

**Fix**:
```python
seen = set()
for item in arr:
    if item not in seen:
        seen.add(item)
```

---

### 15. **Not Freeing Resources**

**Mistake** (worst in C++):
```cpp
Node* node = new Node();
// Forgot delete → memory leak
```

---

### 16. **Silent Bugs in Edge Cases**

**Mistake**:
```python
# Works on normal case
# Breaks on: [], [1], negative numbers
# You didn't test!
```

---

### 17. **Inefficient String Concatenation**

**Mistake**:
```python
result = ""
for char in s:
    result += char  # O(n²) in some languages!
```

**Fix**:
```python
result = ''.join(s)  # O(n)
```

---

### 18. **Deep Copy vs Shallow Copy**

**Mistake**:
```python
new_list = old_list  # Shallow! Changes to old_list affect new_list
```

**Fix**:
```python
new_list = old_list.copy()  # or [:]
```

---

### 19. **Wrong Algorithm for Problem**

**Mistake**: Using linear search where binary search needed  
**Fix**: Recognize problem patterns (sorted → binary search)

---

### 20. **Not Reading Error Messages**

**Mistake**:
```python
# Error: "index out of range"
# You just say "weird bug"
# Should read: INDEX OUT OF RANGE → off-by-one!
```

---

## Prevention Checklist

Before submitting:
- [ ] Tested empty input
- [ ] Tested single element
- [ ] Tested negative numbers
- [ ] Tested duplicates
- [ ] Tested maximum size
- [ ] Complexity stated
- [ ] No mutations during iteration
- [ ] Base cases in recursion
- [ ] Edge case handling
- [ ] Code explanation ready
