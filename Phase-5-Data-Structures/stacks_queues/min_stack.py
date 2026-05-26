"""
Problem: Min Stack
Platform: LeetCode #155
Difficulty: Easy
Link: https://leetcode.com/problems/min-stack/

My thought process:
  Step 1 — Input and output: Stack that supports push, pop, top, getMin.
           getMin must return minimum in O(1) time.
  Step 2 — Brute force: getMin scans entire stack in O(n).
  Step 3 — Why brute force is slow: Every getMin is slow.
  Step 4 — Optimised approach: Use second stack to track minimums.
           When pushing, also push minimum to min_stack.
  Step 5 — Edge cases: All elements same? Negative numbers?

Approach: Two stacks - one for values, one for running minimums
Time complexity:  O(1) for all operations
Space complexity: O(n) — two stacks
"""

class MinStack:
    """Stack that tracks minimum efficiently."""
    
    def __init__(self):
        # Main stack stores all values
        self.stack = []
        # Min stack stores minimums at each level
        # Why: Parallel tracking of minimums
        self.min_stack = []
    
    def push(self, val):
        """Add value to stack."""
        # Add to main stack
        self.stack.append(val)
        
        # Add to min stack
        # Why: Track what the minimum is at this point
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
    
    def pop(self):
        """Remove and return top value."""
        # Remove from both stacks (keep them in sync)
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self):
        """Get top value without removing."""
        return self.stack[-1]
    
    def getMin(self):
        """Get minimum value in O(1)."""
        # Top of min_stack is the current minimum
        return self.min_stack[-1]

# ── Test cases ────────────────────────────
print("Test 1:")
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(f"getMin: {min_stack.getMin()}")  # Expected: -3
min_stack.pop()
print(f"top: {min_stack.top()}")        # Expected: 0
print(f"getMin: {min_stack.getMin()}")  # Expected: -2

print("\nTest 2:")
min_stack2 = MinStack()
min_stack2.push(1)
min_stack2.push(2)
min_stack2.push(3)
print(f"getMin: {min_stack2.getMin()}")  # Expected: 1
min_stack2.pop()
print(f"getMin: {min_stack2.getMin()}")  # Expected: 1

print("\nTest 3:")
min_stack3 = MinStack()
min_stack3.push(5)
min_stack3.push(5)
min_stack3.push(5)
print(f"getMin: {min_stack3.getMin()}")  # Expected: 5
