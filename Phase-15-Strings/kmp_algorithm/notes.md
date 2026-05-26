# KMP (Knuth-Morris-Pratt) Algorithm

## What is KMP?

Pattern matching without backtracking in text.

**Naive**: When mismatch occurs, restart from character 1 of text  
**KMP**: Skip based on pattern overlap analysis

```
Text:    A B C A B D A B A C A B A B
Pattern: A B A C

Naive:
  Try at 0: A B C ✗
  Try at 1: B C A ✗
  Try at 2: C A B ✗
  Try at 3: A B A ✗
  Try at 4: B A C ✗
  ...repeats scanning

KMP:
  Analyzes pattern: "AB" overlaps at start
  When mismatch, skip smartly
  Finds match more efficiently
```

---

## Algorithm Steps

1. **Build failure function** (LPS array)
   - For each position, find longest proper prefix also suffix
   - LPS[i] = longest prefix of pattern[0:i+1] that's also suffix

2. **Search using LPS**
   - Match pattern against text
   - On mismatch, use LPS to skip ahead
   - Don't go back to start of pattern

---

## LPS Array (Longest Proper Prefix-Suffix)

```python
Pattern: "ABABAC"

Index: 0 1 2 3 4 5
Char:  A B A B A C
LPS:   0 0 1 2 3 0

# LPS[5] = 0: "ABABAC" has no prefix that's also suffix
# LPS[4] = 3: "ABABA" has "ABA" as both prefix and suffix
# LPS[3] = 2: "ABAB" has "AB" as both prefix and suffix
```

---

## Time Complexity

- **Build LPS**: O(m) where m = pattern length
- **Search**: O(n) where n = text length
- **Total**: O(n + m) - linear!

This is optimal for pattern matching.
