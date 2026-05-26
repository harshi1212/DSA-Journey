# Communication Checklist (THINK-ALOUD GUIDE)

## Why Communication Matters

- **Code quality**: 50%
- **Communication**: 50%

Bad communication + good code = Medium hire  
Good communication + good code = Strong hire

---

## The STAR Framework

### S - Situation
"I see the problem is about..."

### T - Task
"My task is to..."

### A - Action
"I'll use... algorithm because..."

### R - Result
"This will be O(?) time and O(?) space"

---

## Interview Timeline (45 min)

```
0-3 min:   Clarify problem
3-5 min:   Confirm approach (get approval!)
5-25 min:  Code
25-35 min: Test & optimize
35-40 min: Discuss trade-offs
40-45 min: Q&A
```

---

## Talking Points by Phase

### Phase 1: Clarify (3 min)

**What to say**:
```
"Let me make sure I understand:
- Input: array of integers
- Output: return index of target
- Constraints: 1 ≤ n ≤ 10^5
- Questions:
  - Can array have duplicates?
  - Is array sorted?
  - What to return if not found?"
```

**Why**: Prevents wrong assumptions

---

### Phase 2: Approach (2 min)

**What to say**:
```
"I think the best approach is:
1. Use binary search (since array sorted)
2. Time: O(log n)
3. Space: O(1)

Is this acceptable, or would you prefer something different?"
```

**Why**: Get feedback early, not after coding

---

### Phase 3: Code (15-20 min)

**What to say**:
```
"First, I'll handle edge cases: empty array, single element.
Then I'll initialize left and right pointers.
In each iteration, I'll calculate mid and check..."
```

**Don't**:
- ❌ Code silently
- ❌ Mumble code out loud
- ❌ Explain line-by-line (waste of time)

**Do**:
- ✓ Say function names
- ✓ Explain key logic
- ✓ Think out loud

---

### Phase 4: Test (5-10 min)

**What to say**:
```
"Let me test on a few cases:
1. Normal: [1,3,5], target=3 → index 1 ✓
2. Edge case: [], target=1 → return -1 ✓
3. Not found: [1,3,5], target=2 → return -1 ✓
4. Single: [1], target=1 → index 0 ✓

Great, it works!"
```

**Important**: Trace execution, don't just run code

---

### Phase 5: Optimize (5-10 min)

**What to say**:
```
"Current solution is O(n) time, O(1) space.
Can we do better? 

For sorted array, binary search is O(log n).
This is likely optimal for sorted input.

If input were unsorted, we'd need hashing for O(n) single pass.
But here, O(log n) is best."
```

**Why**: Shows algorithm thinking

---

### Phase 6: Discuss Trade-offs (3-5 min)

**What to say**:
```
"If we need multiple queries, we could:
1. Preprocess to index (O(n) setup, O(1) lookup) - space trade-off
2. Keep current approach (O(log n) per query)

Option 1 if queries >> setup time cost, else Option 2."
```

---

## Key Phrases to Use

### When understanding:
- "Let me clarify..."
- "So the constraint is..."
- "Does this mean...?"

### When proposing:
- "I propose..."
- "One approach is..."
- "This would be O(?) because..."

### When coding:
- "First I'll..."
- "This handles the case where..."
- "Now I'll test..."

### When stuck:
- "Let me think... One solution is brute force O(n²), but better would be..."
- "I'm thinking of... does that sound right?"

### When done:
- "Let me verify with a trace..."
- "The algorithm is O(?) which is..."

---

## Red Flags (Don't Do These)

❌ Code silently for entire interview  
❌ Finish coding, then test (should test continuously)  
❌ Use bad variable names (x, temp, data)  
❌ Forget to handle edge cases  
❌ Claim O(?) complexity but don't justify  
❌ Code, then say "wait, this doesn't work"  
❌ Take 35 minutes on approach, 10 minutes on code  

---

## Green Flags (Do These)

✓ Ask clarifying questions  
✓ Propose approach, get approval  
✓ Explain logic while coding  
✓ Test with concrete examples  
✓ Handle edge cases explicitly  
✓ Analyze complexity correctly  
✓ Discuss trade-offs  
✓ Clean, readable code  

---

## Practice Script

**Time: 5 min**

```
"This is a binary search problem. 
Array is sorted, we need log n search.
First, I'll handle edge cases [empty].
I'll use left/right pointers, binary search.
Time: O(log n), Space: O(1).

[codes for 15 min]

Testing: [1,3,5], target=3 works.
Edge case []: returns -1.
I think this is optimal. 
Any questions or should we move to complexity?"
```

---

## Interviewer Signals

Listen for these:
- "Can you do better?" → You're not optimal yet
- "What about...?" → They want you to consider edge case
- "Good, let's move on" → You're on track
- "Hmm, that won't work because..." → Pivot your approach

**Your job**: Listen and adjust, don't argue
