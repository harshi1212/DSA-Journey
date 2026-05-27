# Phase 8 - Problem-Solving Mindset (Master Guide)

**The meta-skill that makes everything else work. Separates great engineers from good ones.**

---

## Table of Contents
1. [Problem-Solving Framework](#problem-solving-framework)
2. [Reading Problems](#reading-problems)
3. [Understanding Examples](#understanding-examples)
4. [Brainstorming Approaches](#brainstorming-approaches)
5. [Validating Solutions](#validating-solutions)
6. [Interview Communication](#interview-communication)
7. [Common Mistakes](#common-mistakes)
8. [Worked Problems](#worked-problems)

---

# PROBLEM-SOLVING FRAMEWORK

## The 5-Step Framework

**Step 1: Understand (5 min)**
- Read problem 2-3 times
- Identify inputs and outputs
- Clarify constraints and edge cases
- Ask clarifying questions if unclear

**Step 2: Plan (5 min)**
- Brainstorm 3-4 approaches
- Discuss time/space trade-offs
- Choose best approach
- Walk through with example

**Step 3: Implement (10-15 min)**
- Write clean, readable code
- Handle edge cases
- Add comments for clarity
- Compile and run locally first

**Step 4: Test (5 min)**
- Test with provided examples
- Test edge cases (empty, single, large)
- Test boundary conditions
- Check for off-by-one errors

**Step 5: Optimize (5 min)**
- Can you reduce time complexity?
- Can you reduce space complexity?
- Is there a cleaner implementation?

---

## Questioning Protocol

**Must Ask Questions:**
1. "Can I assume the input is valid?" (or validate it?)
2. "What's the range of inputs?" (1 to 10? 1M?)
3. "Are there duplicates?" (in array/string?)
4. "What about empty input?" (array of size 0?)
5. "Do we care about order?" (output specific order?)
6. "Space constraints?" (can we use extra space?)

```python
def ask_clarifying_questions(problem):
    """
    Template for interviewer communication
    """
    questions = {
        "scope": "What's the maximum size of input?",
        "constraints": "Are there duplicates?",
        "edge_cases": "What if input is empty?",
        "requirements": "Should output be sorted?",
        "space": "Can we use extra space?",
        "time": "What's acceptable time complexity?"
    }
    
    return questions
```

---

# READING PROBLEMS

## How to Read Carefully

```
Example Problem:
"Given an array of integers nums and an integer target,
return the indices of the two numbers that add up to target.
You may assume each input has exactly one solution.
Do not use the same element twice."

Key Points to Extract:
1. INPUT: array of integers, integer target
2. OUTPUT: indices (not values!)
3. CONSTRAINT: exactly one solution (simplifies problem)
4. EDGE CASE: can't use same element twice (nums[i] ≠ nums[i])
5. ASSUMPTION: guaranteed valid solution (no need to check)
```

---

## Example-Driven Understanding

```python
def understand_problem(problem_text, examples):
    """
    Work through examples to understand problem
    """
    for i, (input_data, expected_output) in enumerate(examples):
        print(f"Example {i+1}:")
        print(f"  Input: {input_data}")
        print(f"  Expected: {expected_output}")
        
        # Manually trace through
        # What patterns do you see?
        # What changes between examples?
        # Why is that the expected output?

# Example usage:
problem = "Find two numbers that sum to target"
examples = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
]

for inputs, output in examples:
    print(f"Input: {inputs} → Output: {output}")
```

---

# UNDERSTANDING EXAMPLES

## Trace Through Examples

```python
def two_sum(nums, target):
    # Example: nums = [2, 7, 11, 15], target = 9
    # Expected: [0, 1]
    
    # Trace:
    # i=0, nums[0]=2: need 9-2=7
    # i=1, nums[1]=7: found! 2+7=9
    # Return [0, 1]
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Verify with examples
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

for nums, target, expected in test_cases:
    result = two_sum(nums, target)
    status = "✓" if result == expected else "✗"
    print(f"{status} two_sum({nums}, {target}) = {result} (expected {expected})")
```

---

# BRAINSTORMING APPROACHES

## Approach Levels

### Level 1: Brute Force (Always Valid, Often Slow)

```python
def two_sum_brute_force(nums, target):
    """
    Check all pairs
    Time: O(n²)
    Space: O(1)
    
    This ALWAYS works! Use as fallback if stuck.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### Level 2: Optimize with Data Structure

```python
def two_sum_hash(nums, target):
    """
    Use hash map to track seen numbers
    Time: O(n)
    Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Level 3: Problem-Specific Optimization

```python
def two_sum_sorted(nums, target):
    """
    If we CAN sort (check constraints!):
    Time: O(n log n)
    Space: O(1) (sort in-place)
    
    Use two pointers on sorted array
    """
    # Note: Would need to track original indices!
    # Only works if problem doesn't require original indices
    pass
```

---

## Brainstorming Template

```
For any problem:

1. BRUTE FORCE
   - What's the simplest possible approach?
   - Check all combinations? All pairs? All elements?
   - Time/Space?

2. OPTIMIZE SPACE
   - Can a hash map help?
   - Can we track what we've seen?
   - Time/Space?

3. OPTIMIZE TIME
   - Can we sort?
   - Can we use two pointers?
   - Can we precompute?
   - Time/Space?

4. CHOOSE BEST
   - Which approach best fits constraints?
   - Which is cleanest/most readable?
   - Which is most interview-friendly?
```

---

# VALIDATING SOLUTIONS

## Test Case Categories

```python
class TestValidator:
    def test_provided_examples(self, solution, test_cases):
        """Test with examples from problem"""
        for inputs, expected in test_cases:
            result = solution(*inputs)
            assert result == expected, f"Failed: {inputs} → {result} (expected {expected})"
    
    def test_edge_cases(self, solution):
        """Test edge cases"""
        cases = {
            "empty": [],
            "single": [1],
            "all_same": [5, 5, 5],
            "two_elements": [1, 2],
            "very_large": list(range(1000000)),
            "negative": [-1, -2, -3],
            "mixed": [-5, 0, 5, 10],
        }
        
        for name, case in cases.items():
            try:
                result = solution(case)
                print(f"✓ {name}: {result}")
            except Exception as e:
                print(f"✗ {name}: {e}")
    
    def test_boundary_conditions(self, solution):
        """Test boundaries"""
        # Off-by-one errors common here
        cases = [
            [1],           # minimum size
            [1, 2],        # size 2
            list(range(100)),  # larger
        ]
        
        for case in cases:
            result = solution(case)
            assert result is not None, f"Failed for size {len(case)}"
```

---

# INTERVIEW COMMUNICATION

## What Interviewers Listen For

### 1. Clear Explanation
```python
# BAD: "I'll use a hash map"
# GOOD: "I'll use a hash map to store each number and 
#        its index. For each number, I'll check if the
#        complement (target - number) exists in the map."

def explain_approach(approach):
    return f"""
    Approach: {approach['name']}
    
    Idea: {approach['idea']}
    
    Data structures: {approach['data_structures']}
    
    Time: {approach['time']}
    Space: {approach['space']}
    """
```

### 2. Walk Through Example
```python
# GOOD: Explicitly trace through with example
# "Let me trace through [2, 7, 11, 15], target=9:
#  - i=0: num=2, need 7, not in map
#  - Add 2 to map: {2: 0}
#  - i=1: num=7, need 2, found in map!
#  - Return [0, 1]"

def trace_through_example():
    nums = [2, 7, 11, 15]
    target = 9
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        print(f"i={i}, num={num}, need={complement}, seen={seen}")
        
        if complement in seen:
            print(f"Found! {complement} at index {seen[complement]}")
            return [seen[complement], i]
        
        seen[num] = i
    
    return []

trace_through_example()
```

### 3. Handle Interruptions Well
```python
# Interviewer: "Can you optimize this further?"
# GOOD: "Yes! Currently O(n²). We could use a hash map
#        to track seen numbers, reducing it to O(n)."

# Interviewer: "What about edge cases?"
# GOOD: "Good point. Edge cases:
#        - Empty array: return empty
#        - Single element: impossible, return empty
#        - Duplicates: handle correctly with indices
#        - No solution: return empty"

def handle_feedback(feedback):
    responses = {
        "optimize": "We could...",
        "edge_cases": "Edge cases to consider...",
        "complexity": "Time/space tradeoff...",
        "stuck": "Let me think out loud..."
    }
    return responses
```

---

# COMMON MISTAKES

## Mistake 1: Off-By-One Errors

```python
# WRONG: range(len(arr) - 1) - misses last element
for i in range(len(arr) - 1):
    print(arr[i])

# RIGHT: range(len(arr))
for i in range(len(arr)):
    print(arr[i])

# WRONG: Start searching from end when shouldn't
def search_wrong(arr, target):
    for i in range(len(arr) - 1, -1, -1):  # Wrong direction!
        if arr[i] == target:
            return i
    return -1

# RIGHT: Search from beginning
def search_right(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

## Mistake 2: Not Handling Constraints

```python
# WRONG: Assumes no duplicates when there are
def remove_duplicates_wrong(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Actually works! But if constraint is "in-place"...
# WRONG for in-place
def remove_duplicates_wrong_inplace(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)  # Creates new list!
    return unique

# RIGHT for in-place (with sorted array)
def remove_duplicates_right(arr):
    if not arr:
        return 0
    
    write_idx = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            write_idx += 1
            arr[write_idx] = arr[i]
    
    return write_idx + 1
```

---

## Mistake 3: Inefficient Approaches

```python
# WRONG: O(n²) when O(n) possible
def find_sum_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

# RIGHT: O(n) with hash map
def find_sum_fast(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

---

# WORKED PROBLEMS

## Problem 1: Two Sum II (Sorted Array)

```python
def two_sum_sorted(numbers, target):
    """
    Input: SORTED array, target
    Output: Indices (1-indexed!)
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed!
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Test
print(two_sum_sorted([2, 7, 11, 15], 9))   # [1, 2]
print(two_sum_sorted([2, 3, 4], 6))        # [1, 3]
```

---

## Problem 2: Container With Most Water

```python
def max_area(height):
    """
    Find two lines that form container with max area
    
    Approach: Two pointers converging
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(height) - 1
    max_area_val = 0
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_area_val = max(max_area_val, current_area)
        
        # Move pointer pointing at shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area_val

# Test
print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
print(max_area([1,1]))                  # 1
```

---

**Master the problem-solving framework. It matters more than knowing algorithms.** 🎯

