# Quick Interview Prep (1-2 Hours Before)

**Goal**: Calm nerves, activate knowledge, build confidence  
**Time**: 60-90 minutes

---

## 15 MIN: Mental Reset

### Breathing Exercise (2 min)
```
4-4-4 breathing:
- Inhale for 4 seconds
- Hold for 4 seconds
- Exhale for 4 seconds
Repeat 5 times
```

### Positive Affirmations (2 min)
Say out loud:
- "I've solved 100+ problems, I can do this"
- "The interviewer wants me to succeed"
- "I'll think out loud and ask for help"
- "Off-by-one errors, edge cases - I've got this"

### Review Your Wins (11 min)
List on paper:
- 3 problems you solved recently
- 3 algorithms you mastered
- 3 times you debugged successfully

---

## 20 MIN: Algorithm Activation

Pick ONE weakness and master it for 5 min each:

### ⭐ If Weak in Binary Search
```python
# Template:
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
```
**Test**: [1,3,5,7], target=5 → should return 2 ✓

### ⭐ If Weak in Hash Maps
```python
# Pattern:
def solve(arr):
    seen = {}
    for num in arr:
        if num in seen:
            # Found duplicate/pair
            pass
        seen[num] = True
    return result
```
**Test**: [1,2,3,2], find duplicate → should find 2 ✓

### ⭐ If Weak in DFS
```python
# Template:
def dfs(node):
    if not node:
        return
    # Process node
    dfs(node.left)
    dfs(node.right)
    return result
```
**Test**: Traverse simple tree ✓

### ⭐ If Weak in Two Pointers
```python
# Pattern:
def solve(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if condition:
            left += 1
        else:
            right -= 1
    return result
```
**Test**: Find palindrome substring ✓

### ⭐ If Weak in Dynamic Programming
```python
# Template:
def solve(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    return dp[-1]
```
**Test**: Max subarray [−2,1,−3,4,−1,2] → should return 6 ✓

### ⭐ If Weak in Graphs
```python
# Template (BFS):
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```
**Test**: Simple graph, count connected ✓

---

## 15 MIN: Code Template Review

Open your best template file and memorize ONE template:

**Pick based on company**:
- Google? → Binary search, segment tree
- Meta? → Graph, BFS/DFS
- Amazon? → DP, hash map
- Microsoft? → Two pointers, sliding window

Code it from memory in 3-5 minutes.

---

## 15 MIN: Mock Problem (Easy)

Solve **ONE easy problem** completely:

**Example Easy Problem**:
```
Problem: Two Sum
Input: [2, 7, 11, 15], target = 9
Output: [0, 1]

Solve in 5 min:
- Understand: Find indices of two numbers that sum to target ✓
- Hash map: {2: 0, 7: 1}
- One pass: For each num, check if (target - num) in map ✓
- Code: 5 lines ✓
- Test: Works on [2,7,11,15] ✓

BOOM. Confidence up 50% ✓
```

---

## 10 MIN: Mental Checklist Review

Repeat this checklist in your head:

**During Problem Solving**:
- [ ] Ask clarifying questions (30 sec)
- [ ] Explain approach (1 min)
- [ ] Get approval before coding
- [ ] Code thinking-aloud
- [ ] Test with example
- [ ] Check edge cases: [], [1], negative, duplicates
- [ ] Verify complexity
- [ ] Discuss trade-offs

**If Stuck**:
- [ ] Ask for hint (no shame!)
- [ ] Think out loud (interviewer helps if they hear you)
- [ ] Start with brute force (O(n²) is better than nothing)
- [ ] Move on if takes >3 min (don't waste time)

**Communication**:
- [ ] Say: "I see... let me clarify"
- [ ] Say: "I'll use X because..."
- [ ] Say: "This handles the case where..."
- [ ] Say: "Let me trace through..."
- [ ] Say: "The complexity is O(?) because..."

**Never Say**:
- ❌ "I don't know"
- ❌ "This should work" (without testing)
- ❌ "I forgot how to code this"
- ❌ Silence for >2 minutes

---

## 5 MIN: Calm Your Brain

### Visual Anchor (3 min)
Close eyes and visualize:
1. Walking into interview room ✓
2. Shaking hands, sitting down ✓
3. Reading problem ✓
4. Saying "Let me clarify..." ✓
5. Solving problem ✓
6. Interviewer smiling, saying "Great solution" ✓

Feel the confidence! 💪

### Power Pose (2 min)
Stand up straight for 2 minutes:
- Shoulders back
- Chest open
- Hands on hips or raised

Research shows: This releases confidence hormones!

---

## Final Check (5 min)

Before leaving for interview:

- [ ] Have water (sip before starting, calm voice)
- [ ] Have notepad + pen (write variable names, trace)
- [ ] Have ID + phone
- [ ] Internet working (for video interview)
- [ ] Quiet place (no distractions)

---

## IF NERVOUS: Quick Grounding

**5-4-3-2-1 Technique**:
- See 5 things around you
- Touch 4 things (texture)
- Hear 3 sounds
- Smell 2 things
- Taste 1 thing

**Takes 2 minutes, resets anxiety**

---

## HOUR-BY-HOUR BREAKDOWN

### 2 Hours Before
- Review cheatsheet (10 min)
- Do one complete mock (20 min)
- Relax, eat snack (30 min)

### 1 Hour Before
- Review weakness algorithm (5 min)
- Review one code template (5 min)
- Breathing exercise (5 min)
- Positive affirmations (5 min)
- Final visualization (5 min)
- Hydrate, bathroom, relax (30 min)

### 10 Minutes Before
- Quick mental checklist review (3 min)
- Power pose (2 min)
- Deep breaths (2 min)
- Ready! Let's go! 🚀

---

## COMMON INTERVIEW QUESTIONS (Be Ready!)

Interviewer will likely ask:

### Q1: "Tell me about yourself" (2-3 min)
**Answer template**:
```
"I'm a computer science student focused on DSA.
I've solved 100+ problems across all patterns.
I'm particularly strong in [your strongest area].
In interviews, I focus on communicating clearly
and finding optimal solutions. I'm ready to learn!"
```

### Q2: "Why this company?"
**Answer template**:
```
"I admire your technology/problems.
Your recent work in [area] aligns with my interests.
I want to grow as an engineer here."
```

### Q3: "What's your weakest area?"
**Answer template**:
```
"I find [area] challenging, but I've been practicing.
I recently solved [problem] which helped me improve.
I ask questions when stuck and learn quickly."
```

### Q4: "Any questions for me?"
**Good questions**:
- "What's a typical problem set size?"
- "What's the team structure?"
- "What does success look like in this role?"
- "What's your favorite part of working here?"

---

## SUCCESS METRICS FOR THIS SESSION

After 1-2 hours, you should feel:

✓ Calm (breathing regulated)  
✓ Confident (did mock problem)  
✓ Prepared (reviewed key algorithms)  
✓ Ready (visualization done)  
✓ Energized (power pose!)  

If yes on 4/5: You're ready! 🎯

---

## REMEMBER

**The interview is not a test. It's a conversation.**

Interviewers:
- Want you to succeed
- Help if you're stuck
- Judge on thinking, not just code
- Value communication over silence

**You've got this, Harshi! 💪**

Go solve that problem and get the offer! 🚀
