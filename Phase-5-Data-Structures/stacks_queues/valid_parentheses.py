"""
Problem: Valid Parentheses
Platform: LeetCode #20
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

My thought process:
  Step 1 — Input and output: String with brackets. 
           Check if all brackets are properly matched and ordered.
  Step 2 — Brute force: Multiple passes checking pairs.
  Step 3 — Why brute force is slow: Multiple iterations needed.
  Step 4 — Optimised approach: Use stack.
           Push opening brackets, pop when seeing closing.
           Match types must be correct.
  Step 5 — Edge cases: Empty string? Odd number of brackets?

Approach: Stack to track opening brackets, match with closing
Time complexity:  O(n) — one pass through string
Space complexity: O(n) — stack stores opening brackets
"""

def isValid(s):
    """
    Check if string has valid matching parentheses/brackets.
    """
    # Stack to store opening brackets
    # Why: Match closing with most recent opening
    stack = []
    
    # Map closing brackets to opening brackets
    # Why: Know which opening matches which closing
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching:
            # It's a closing bracket
            
            # Check if stack is empty (can't close if nothing open)
            if not stack:
                return False
            
            # Get the most recent opening bracket
            top = stack.pop()
            
            # Does it match the closing bracket?
            if top != matching[char]:
                return False
        else:
            # It's an opening bracket, add to stack
            stack.append(char)
    
    # At the end, stack should be empty (all closed)
    return len(stack) == 0

# ── Test cases ────────────────────────────
print("Test 1:")
s = "()"
print(f"Input: '{s}'")
print(f"Output: {isValid(s)}")  # Expected: True

print("\nTest 2:")
s = "()[]{}"
print(f"Input: '{s}'")
print(f"Output: {isValid(s)}")  # Expected: True

print("\nTest 3:")
s = "([)]"
print(f"Input: '{s}'")
print(f"Output: {isValid(s)}")  # Expected: False (wrong order)

print("\nTest 4:")
s = "([{}])"
print(f"Input: '{s}'")
print(f"Output: {isValid(s)}")  # Expected: True

print("\nTest 5 (Edge case):")
s = "("
print(f"Input: '{s}'")
print(f"Output: {isValid(s)}")  # Expected: False (unclosed)
