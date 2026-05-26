# Edge Case Detection Guide

## What Are Edge Cases?

Boundary conditions, special inputs that might break your solution.

---

## Categories of Edge Cases

### 1. **Empty/Null Cases**

```python
# Always check these:
- Empty array []
- Single element [x]
- Empty string ""
- None/null references
- Empty graph (0 nodes)
```

**When to check**: Always first thing

### 2. **Boundary/Limit Cases**

```python
- Very large numbers (overflow concerns)
- Very small numbers (negative, zero)
- Maximum array/string length
- Maximum/minimum values in constraints
```

**Example**:
```python
# Sort problem with n=100,000
# Test with: n=1, n=100,000
```

### 3. **Off-by-One Cases**

```python
- Array indexing (0 vs 1-indexed)
- Inclusive vs exclusive ranges
- Loop boundaries (< vs <=)
```

**Example**:
```python
# Range [1, 5]
# Off-by-one: includes 5 or not?
```

### 4. **Duplicate/Frequency Cases**

```python
- All elements same [1, 1, 1]
- All elements unique [1, 2, 3]
- Many duplicates, few unique
```

### 5. **Negative/Sign Cases**

```python
- All negative [-5, -2, -1]
- Mixed positive/negative [-2, -1, 0, 1, 2]
- Zero [0, 0, 0]
```

### 6. **Special Patterns**

```python
# For specific problems:
String: palindrome, single char, no spaces
Array: sorted, reverse sorted, rotated
Graph: disconnected, self-loops, no edges
Tree: single node, skewed (all left/right)
```

---

## Detection Strategy (Use This!)

```python
def solve(arr):
    # BEFORE coding, list edge cases:
    # 1. Empty: []
    # 2. Single: [1]
    # 3. Duplicates: [1, 1, 1]
    # 4. Large: [1..100000]
    # 5. Negative: [-5, -2, 0]
    
    # Then code...
    pass

# AFTER coding, TEST all:
test_cases = [
    [],
    [1],
    [1, 1, 1],
    list(range(1000)),
    [-5, -2, 0, 2, 5],
]
```

---

## Algorithm-Specific Edge Cases

### Arrays/Sorting
- Empty
- Single element
- All same
- Already sorted
- Reverse sorted
- Duplicates

### Strings
- Empty
- Single char
- All same char
- Palindrome
- No spaces/special chars

### Trees
- Single node
- All left (skewed)
- All right (skewed)
- Balanced
- No children

### Graphs
- Single node
- No edges
- Disconnected
- Self-loops
- Multiple edges

---

## Testing Checklist

Before submitting, test:
- [ ] Empty input
- [ ] Single element
- [ ] Maximum size
- [ ] All duplicates
- [ ] Boundary values (0, -1, INT_MAX)
- [ ] Special patterns (sorted, rotated, etc.)

**Time spent**: 3-5 minutes  
**Bugs caught**: 50-80%
