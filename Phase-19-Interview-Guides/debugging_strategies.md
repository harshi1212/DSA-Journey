# Debugging Strategies Guide

## Under Pressure: Stay Calm

Debugging in interview ≠ debugging at home

- **No IDE debugger**
- **No print statements** (usually)
- **Time pressure** (15 min left?)
- **Interviewer watching**

---

## Strategy 1: Trace Execution (Most Effective)

**Method**: Write out state at each step

```python
# Code:
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

# Test: binary_search([1, 3, 5, 7], 5)

# Trace:
# Initial: left=0, right=3, target=5
# Step 1: mid=1, arr[1]=3 < 5 → left=2
# Step 2: mid=2, arr[2]=5 == 5 → return 2 ✓
```

**When to use**: Suspected off-by-one, wrong logic

---

## Strategy 2: Edge Case Test

**Method**: Run on boundary cases

```python
# Instead of tracing:
test_cases = [
    ([], 5, -1),           # Empty
    ([1], 1, 0),           # Single element
    ([1, 3, 5], 0, -1),    # Not found
    ([1, 3, 5], 5, 2),     # Last element
    ([1, 3, 5], 1, 0),     # First element
]

for arr, target, expected in test_cases:
    result = binary_search(arr, target)
    if result != expected:
        print(f"FAIL: {arr}, {target} → {result}, expected {expected}")
```

**When to use**: Already coded, want quick check

---

## Strategy 3: Print Key Variables (Ask First!)

**Method**: Ask if you can add prints

```python
"I want to add print statements to trace:
- What's mid value?
- How many iterations?
- When left/right change?

Can I do that?"
```

**When to use**: Complex algorithm, need visibility

---

## Strategy 4: Rubber Duck Debugging

**Method**: Explain code line-by-line to interviewer

```python
You: "So I initialize left to 0, right to length-1.
     Then while left <= right, I calculate mid..."

Interviewer: "Wait, why <= instead of <?"

You: "Oh! If only <, then when left==right, I miss the element!
     Good catch, it should be <=."
```

**When to use**: Can't find bug visually, need fresh eyes

---

## Strategy 5: Compare with Expected

**Method**: Manually calculate expected, compare

```python
# Problem: "Count palindromic substrings"
# Test: "aba"
# Expected: "a", "b", "a", "aba" = 4

# Your output: 3
# Bug: Forgot to count single characters!
```

**When to use**: Know correct answer, your output differs

---

## Common Bugs and Catches

### Bug: Off-by-one in loop

**Symptom**: Missing last element, goes too far

**Fix**:
```python
# Wrong:
for i in range(n):    # Goes 0 to n-1
    process(arr[i+1]) # Tries arr[n], crashes!

# Right:
for i in range(n-1):
    process(arr[i+1])
```

**Debug**: Print i when accessing

---

### Bug: Wrong comparison operator

**Symptom**: Finds wrong element, returns incorrect

**Fix**:
```python
# Wrong:
if arr[mid] < target:     # Off by one?
    left = mid

# Right:
if arr[mid] < target:
    left = mid + 1
```

**Debug**: Trace with example [1,3,5], target=3

---

### Bug: Forgot base case

**Symptom**: Infinite recursion, crashes

**Fix**:
```python
# Wrong:
def factorial(n):
    return n * factorial(n-1)  # No base case!

# Right:
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

**Debug**: Does recursion terminate?

---

### Bug: Mutating input

**Symptom**: Works first time, second call fails

**Fix**:
```python
# Wrong:
def process(arr):
    arr.sort()  # Mutates input!
    return result

# Right:
def process(arr):
    sorted_arr = sorted(arr)  # Copy
    return result
```

**Debug**: Is input changing?

---

### Bug: Wrong data type

**Symptom**: Type error, crashes on operation

**Fix**:
```python
# Wrong:
count = "0"
count += 1  # TypeError: can't add int to str

# Right:
count = 0
count += 1
```

**Debug**: Print type of variable

---

## Debugging Checklist (2 min)

Before crying "It doesn't work!":

- [ ] Did you test with empty input?
- [ ] Did you test with single element?
- [ ] Did you test with negative numbers?
- [ ] Are off-by-one possibilities checked?
- [ ] Did you trace one full execution?
- [ ] Does recursion have base case?
- [ ] Are you mutating input?
- [ ] Is loop condition correct?
- [ ] Are array bounds safe?

---

## What to Say When You Find Bug

**Good**:
```
"Oh, I see the issue! When I'm at the last element,
the loop tries to access arr[i+1] which is out of bounds.
I should use range(n-1) instead of range(n)."
```

**Not good**:
```
"Uhh, it's broken."
```

**Interviewer thinks**: "Can this person debug?"

---

## Worst Case: Can't Find Bug

**What to say**:
```
"I know the algorithm should work. Let me trace through
one more example manually... 

If I can't find it in next 2 minutes, I think it's likely
an off-by-one or edge case I'm missing. In a real interview,
I'd add prints or use a debugger. Should I code the fix
I suspect, or do you see what I'm missing?"
```

**Interviewer**: Usually hints at this point

---

## Prevention > Debugging

**Best strategy**: Code carefully first time
- Think through logic before typing
- Handle edge cases upfront
- Test as you code

**Second best**: Quick trace after coding
- Trace with simple example
- Catch 80% of bugs in 2 minutes

**Last resort**: Ask for help
- Show you can think through it
- Get hint to progress
