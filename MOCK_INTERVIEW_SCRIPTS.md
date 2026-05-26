# 🎤 Mock Interview Scripts

**Exact words to say in interviews. Communication frameworks with verbatim responses.**

---

## Setup: Before Interview Starts

### Opening Script

**Interviewer:** "Hi! Thanks for joining. Let's dive in. Here's your problem..."

**You say:**
```
"Thanks for having me! I'm excited to work through this problem.
Let me take a moment to understand the problem, then I'll walk you
through my approach before coding. Does that sound good?"
```

**Why it works:** Shows structure, buys thinking time, confirms expectations

---

### When You Don't Understand

**Interviewer:** "Find the longest substring without repeating characters."

**You say (if unclear):**
```
"Just to clarify: are we looking for a substring (contiguous) or
a subsequence (can skip characters)? And should I consider Unicode
characters or just ASCII?"
```

**Why it works:** Clarifies ambiguity, shows attention to detail, prevents wrong solution

---

## Talking Through Problems

### Pattern 1: Two Pointers Problem

**Interviewer:** "Given a sorted array, find two numbers that sum to target."

**Your Script:**
```
"Let me break this down:
- Input: sorted array, target number
- Output: indices of two numbers summing to target
- Constraints: should we handle duplicates?

My approach: Use two pointers - one at start, one at end.
If sum is too small, move left pointer right.
If sum is too large, move right pointer left.
This works because array is sorted.

Let me trace through with [1,2,3,4,5], target=7:
- Start: left=0 (1), right=4 (5), sum=6 < 7, move left
- Next: left=1 (2), right=4 (5), sum=7 ✅ Found!

Time: O(n) - one pass
Space: O(1) - only pointers
```

**Why structured:**
- Problem clarification (what exactly?)
- Approach explanation (why this method?)
- Example walkthrough (how does it work?)
- Complexity analysis (is it efficient?)

---

### Pattern 2: DP Problem

**Interviewer:** "How many ways to climb stairs if you can take 1 or 2 steps?"

**Your Script:**
```
"Let me think about this:
- Base case: 1 stair = 1 way (take 1 step)
                2 stairs = 2 ways (1+1 or 2)
                
- Recurrence: To reach stair n, I could have come from:
              stair (n-1) with 1 step, OR
              stair (n-2) with 2 steps
              
  So ways(n) = ways(n-1) + ways(n-2)
  
- Build table bottom-up:
  n:    1   2   3   4   5
  ways: 1   2   3   5   8
  
- For 5 stairs: 8 ways total

Time: O(n) - calculate each stair once
Space: O(n) - array to store, could optimize to O(1)
```

**Why it works:**
- Shows mathematical thinking
- Explains recurrence relation
- Demonstrates table building
- Acknowledges optimization opportunities

---

### Pattern 3: Graph/Tree Problem

**Interviewer:** "Check if binary tree is balanced."

**Your Script:**
```
"Definition clarification first: balanced means the height difference
between left and right subtree is at most 1, for every node?

My approach:
1. DFS from root
2. For each node, check:
   - Is left subtree balanced?
   - Is right subtree balanced?
   - Is height difference ≤ 1?
3. Return true only if all conditions met

Let me code this:

def isBalanced(node):
    if not node:
        return True, 0  # (balanced, height)
    
    left_balanced, left_height = isBalanced(node.left)
    right_balanced, right_height = isBalanced(node.right)
    
    is_balanced = (left_balanced and right_balanced and 
                   abs(left_height - right_height) <= 1)
    
    height = max(left_height, right_height) + 1
    
    return is_balanced, height

Time: O(n) - visit each node once
Space: O(h) - recursion stack, h = height
"
```

---

## When You Get Stuck

### Stuck Script #1: "Let me think out loud"

**You say:**
```
"I'm going to think through this out loud. I have a brute force
approach that works - iterate all pairs, check sum.
That's O(n²) time. Let me see if I can optimize...

[talking through optimization]

Actually, a hash map would work! As I iterate, store seen numbers.
For each number, check if (target - number) in hash map.
That's O(n) time now. Is this optimization worth mentioning?"
```

**Why it works:**
- Shows thinking process
- Acknowledges brute force first
- Demonstrates optimization thinking
- Asks for validation

---

### Stuck Script #2: "Can I clarify constraints?"

**You say:**
```
"I want to make sure I'm solving the right problem.

Can we confirm:
1. What's the input size? (affects whether O(n²) is acceptable)
2. Is there a time constraint?
3. Can I modify the input array or must it remain unchanged?
4. Should I handle negative numbers, zeros?

This will help me choose between solutions."
```

**Why it works:**
- Buys thinking time
- Shows consideration of constraints
- Demonstrates that tradeoffs depend on constraints

---

### Stuck Script #3: "Let me simplify first"

**You say:**
```
"This problem seems complex. Let me start with a simpler case.

What if array had no duplicates?
[Then solve simplified version]

Now, how does adding duplicates change the solution?
[Add complexity incrementally]

The key insight is [state insight]. Now I can generalize..."
```

**Why it works:**
- Reduces cognitive load
- Shows decomposition skill
- Builds from simple to complex
- Demonstrates clarity of thinking

---

## During Coding

### Narration While Coding

**You say (as you type):**
```
"First, I'll check edge cases - empty array, single element.

Then I'll initialize: left pointer at start, right at end.

Now the main loop: while left < right:
  - Calculate sum
  - Adjust pointers based on sum vs target
  - When sum equals target, return pair

Finally, if no pair found, return empty or -1.

Let me trace through once before running..."
```

**Why it works:**
- Interviewer understands your thinking
- Shows you're considering all cases
- Easier to debug if code has issues
- Demonstrates communication skill

---

### When You Make a Mistake

**You say:**
```
"Wait, I made an error - I'm incrementing the wrong pointer.
Let me fix that. It should be [correction].

Good catch - let me retrace with the fixed code..."
```

**Why it works:**
- Shows self-correction ability
- Demonstrates code review skills
- Reduces panic, shows confidence

---

## Problem Classification Scripts

### "This is a Pattern I Recognize"

**You say:**
```
"This problem looks like a [pattern name] problem.

[Pattern name] problems typically:
- Have characteristic [feature 1]
- Require [technique 1]
- Common time complexity [expected]

The approach is:
[Explain approach]

I've seen this pattern in [related problem], and the technique applies here too."
```

**Pattern Examples to Mention:**
```
"This is a sliding window problem..."
"This looks like binary search..."
"This is a classic two-pointer scenario..."
"This seems like a DP problem..."
"This is a backtracking problem..."
"This requires a graph traversal..."
"This is a greedy algorithm situation..."
```

**Why it works:**
- Shows pattern recognition
- Demonstrates you've practiced
- Applies known solution
- Increases confidence

---

## Handling Interviewer Questions

### "Can you optimize further?"

**Script:**
```
"Yes! Currently we're O(n²) time. Let me think...

[Mention current approach limitations]

Actually, if we use [data structure], we could:
[Explain optimization]

This would be O(n) time, O(n) space tradeoff.

Should we go with this approach, or is current solution acceptable?"
```

---

### "What about edge cases?"

**Script:**
```
"Great question! Let me think through edge cases:

1. Empty input - should return [what]
2. Single element - should return [what]
3. All duplicates - should handle by [method]
4. Negative numbers - algorithm still works because [reason]
5. Very large input - O(n) should handle up to [size]

Let me add checks for cases 1 and 2:
[Show code for handling]
"
```

---

### "What's the time complexity?"

**Script:**
```
"The time complexity is O(n log n).

Here's why:
- We have outer loop: O(n)
- Inside each iteration: binary search which is O(log n)
- Combined: O(n × log n) = O(n log n)

Space complexity is O(1) - only using pointers, no extra arrays."
```

**When uncertain:**
```
"Let me trace through:
- Outer loop runs [n] times
- Inner loop runs at most [n] times
- So total operations: O(n²)

Actually, with the optimization, inner loop is O(log n), so O(n log n)."
```

---

### "Can you walk me through your code?"

**Script:**
```
"Sure! Let me trace through this example step by step.

Input: [1,3,5,7], target=8

Line 1-2: Initialize left=0, right=3
Line 4: Enter while loop (0 < 3)
Line 5: sum = arr[0] + arr[3] = 1 + 7 = 8
Line 6: sum == target, so return [0, 3]

And that's the answer!

If I try another example where they don't match..."
```

---

## Ending the Interview

### "Do you have questions for me?"

**Good responses:**
```
"Yes! I'd love to know:
1. What was most challenging about this problem?
2. What would be the next iteration if this was production code?
3. How do you typically approach problem-solving here?"
```

**Avoid:**
```
❌ "No questions"
❌ "When do I hear back?"
❌ Long silence
```

---

### Ending Script

**You say:**
```
"Thanks for the great problem! I enjoyed working through the optimization
and tradeoffs. I appreciate the feedback on [something specific].

I'm excited about the work you're doing with [company detail], 
especially [genuine interest].

Let me know if you need anything else from me!"
```

---

## Common Mistakes to Avoid

### ❌ DON'T Say

```
"Uh... let me think..."  (vague, sounds uncertain)
"I don't know"           (without trying)
"This is hard"           (negative)
"I usually just..."      (no structure)
"Let me start coding"    (without planning)
"Is this right?"         (seeking validation every line)
```

### ✅ DO Say

```
"Let me clarify the problem..."     (seeking understanding)
"Here's my approach..."             (structured)
"I can do this two ways..."         (showing options)
"Let me trace through with..."      (demonstrating)
"The time complexity is..."         (technical)
"This could be optimized to..."     (awareness)
```

---

## Full Interview Simulation

**Total Duration: 45 minutes**

```
0-2 min:   Greeting + Problem statement
3-5 min:   Clarify requirements
6-12 min:  Discuss approach
13-30 min: Implement + narrate
31-40 min: Test + debug
41-45 min: Optimize + discuss tradeoffs
```

**Key Timing:**
- Spend 30% time understanding
- Spend 50% time coding
- Spend 20% time testing/optimization

---

## Confidence Boosters

**Before Interview, Say to Yourself:**
```
"I've practiced this pattern 10+ times.
I can break complex problems into steps.
I know how to communicate my thinking.
Mistakes are learning opportunities.
I'm prepared for this."
```

**During Interview, If Nervous:**
```
"Breathe. Think out loud. Ask clarifying questions.
It's okay to take a moment. The interviewer wants me to succeed."
```

---

**Use these scripts. Practice out loud. Adapt to your style. Nail the interview.** 🎯

