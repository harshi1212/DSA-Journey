# Phase 10 - Mock Interviews & Interview Simulation

**Simulate real interviews. Practice under pressure conditions.**

---

## Interview Format Understanding

**Typical Technical Interview (45-60 minutes):**
- 5 min: Introductions, warm-up
- 5 min: Problem explanation
- 35 min: Problem solving
- 5 min: Complexity discussion
- 10 min: Questions for interviewer

---

## Mock Interview #1: Two Sum (Easy)

**Problem:** "Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target."

**Solution Script:**

```
INTRODUCTION (30 sec):
"Hi! Thanks for having me. I'm excited to discuss this problem.
Let me make sure I understand: We need to find indices of two numbers
that sum to a target, and each element used once?"

CLARIFYING QUESTIONS (2 min):
- "Can I assume there's exactly one solution?"
- "Should output be in any specific order?"
- "What's the constraint on array size?"
- "Can input have duplicates?"

APPROACH DISCUSSION (3 min):
"I see a few approaches:

1. Brute Force: Check all pairs - O(n²) time, O(1) space
2. Hash Map: Store seen numbers - O(n) time, O(n) space
3. Sort + Two Pointers: O(n log n) time, O(1) space (but loses indices)

I'll go with approach 2 - hash map - because it's O(n) time
and we need to return indices anyway."

WALK THROUGH EXAMPLE (3 min):
"Let me trace through [2, 7, 11, 15], target = 9:
- i=0: num=2, need=7, seen={}. Add 2.
- i=1: num=7, need=2. Found 2 in seen at index 0!
- Return [0, 1]"

IMPLEMENTATION (5 min):
```
def twoSum(nums, target):
    seen = {}  # num -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []
```

TESTING (2 min):
"Test cases:
- [2,7,11,15], 9 → [0,1] ✓
- [3,3], 6 → [0,1] ✓
- [3], 3 → [] ✓ (need two numbers)"

COMPLEXITY ANALYSIS (1 min):
"Time: O(n) - single pass
Space: O(n) - hash map stores up to n elements"
```

---

## Mock Interview #2: LRU Cache (Medium)

**Problem:** "Design an LRU (Least Recently Used) Cache."

**Solution Script:**

```
UNDERSTANDING (2 min):
"LRU Cache should support:
1. get(key) - return value if exists, -1 if not
2. put(key, value) - set value, evict LRU if full
Both should be O(1)"

APPROACH (3 min):
"I'll use:
1. Hash Map: O(1) lookup/insert/delete by key
2. Doubly Linked List: O(1) reordering (move to front)

Most recently used → head
Least recently used → tail (evict from tail)

When get/put: move to head
When full: remove tail"

IMPLEMENTATION (8 min):
```
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```

WALK THROUGH (2 min):
"With capacity 2:
- put(1, 1): {1:1} → 1
- put(2, 2): {1:1, 2:2} → 1-2
- get(1): {1:1, 2:2} → 2-1 (1 moved to end)
- put(3, 3): {1:1, 3:3} → 1-3 (2 evicted, LRU)"

COMPLEXITY (1 min):
"Time: O(1) for all operations
Space: O(capacity)"
```

---

## Common Interview Traps

**Trap 1: Off-by-One Errors**
```python
# Wrong
for i in range(len(arr) - 1):  # Misses last element

# Right
for i in range(len(arr)):  # Includes all
```

**Trap 2: Forgetting Edge Cases**
```python
# Must handle:
if not arr:      # Empty
if len(arr) == 1:  # Single element
if len(arr) == 2:  # Minimum for pairs
```

**Trap 3: Wrong Complexity Analysis**
```python
# Claims O(n) but it's O(n²)
for num in arr:
    for other in arr:  # Nested loop!
        if num == other:
            pass

# Always verify: "For each element, I'm doing what?"
```

---

## Interview Red Flags (Avoid These!)

```python
# ✗ Hard-coded array indices
arr[0], arr[1], arr[2]  # Won't work for different sizes

# ✗ Modifying input when shouldn't
nums.sort()  # If problem says "do not modify"

# ✗ Using wrong data structure
arr.pop(0)  # O(n)! Use deque for O(1)

# ✗ Not testing edge cases
# Solution works for [1,2,3] but fails for []

# ✗ Not explaining approach
# Jumping straight to code confuses interviewer

# ✗ Wrong complexity declaration
# "This is O(n)" but algorithm is O(n²)
```

---

## Interview Success Checklist

```
Before interview:
☐ Sleep well
☐ Eat something
☐ Test computer/audio
☐ Have pen and paper

During interview:
☐ Ask clarifying questions (don't assume)
☐ Discuss approach before coding
☐ Think out loud (let them hear your thought process)
☐ Write clean, readable code (not golf code!)
☐ Test with provided examples
☐ Test with edge cases
☐ Explain complexity (time AND space)
☐ Be ready for "Can you optimize?"
☐ Ask good questions at the end

After interview:
☐ Review what you did well
☐ Identify what to improve
☐ Practice similar problems
```

---

## Questions to Ask Interviewer

**Good Questions:**
- "What's the size of data in production?"
- "Can you walk me through how this would be used?"
- "What's most important - time or space?"
- "How would this scale if requirements changed?"
- "What technologies do you use?"
- "What's the team structure like?"
- "What's the biggest challenge your team faces?"

**Avoid:**
- "How much vacation?" (until offer stage)
- "When will I be promoted?" (too early)
- Anything about money (until offer)

---

## Interview Scoring Rubric

**Communication (20%)**
- ☐ Clear explanations
- ☐ Asks clarifying questions
- ☐ Thinks out loud
- ☐ Listens to feedback

**Problem-Solving (30%)**
- ☐ Correct solution
- ☐ Handles edge cases
- ☐ Identifies approach
- ☐ Can optimize

**Code Quality (30%)**
- ☐ Readable code
- ☐ Proper variable names
- ☐ No bugs
- ☐ Follows conventions

**Complexity Analysis (20%)**
- ☐ Correct time complexity
- ☐ Correct space complexity
- ☐ Can explain trade-offs
- ☐ Optimization ideas

**Passing Score: 75%+ (45+ points)**

---

## 30-Day Interview Prep

**Week 1: Foundations**
- Day 1-2: Two Sum, Valid Parentheses
- Day 3-4: Best Time to Buy Stock, Majority Element
- Day 5-7: Practice mock interviews with 3 easy problems

**Week 2: Intermediate**
- Day 8-9: 3Sum, Container with Most Water
- Day 10-11: Longest Substring, Min Window
- Day 12-14: Practice mock interviews with 3 medium problems

**Week 3: Advanced**
- Day 15-16: LRU Cache, Course Schedule
- Day 17-18: Word Ladder, Number of Islands
- Day 19-21: Practice mock interviews with 2 hard, 1 medium

**Week 4: Timed Practice**
- Day 22-30: Full interviews, 45 min per problem
- Mix: 2 easy, 3 medium, 2 hard, 1 system design

---

**Practice interviews until you're confident under pressure.** 🎯

