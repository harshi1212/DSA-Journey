"""
Problem: Two Sum
Platform: LeetCode #1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

My thought process:
  Step 1 — Input and output: Array of integers, target sum. 
           Return indices of two numbers that add up to target.
  Step 2 — Brute force: Check every pair of numbers.
  Step 3 — Why brute force is slow: O(n²) - nested loops.
  Step 4 — Optimised approach: Hash map to store seen numbers.
           For each number, check if (target - number) exists.
  Step 5 — Edge cases: What if no solution? What if same number twice?

Approach: Use hash map to store value→index, find complement in O(1)
Time complexity:  O(n) — one pass through array
Space complexity: O(n) — hash map stores n elements
"""

def twoSum(nums, target):
    """
    Find two numbers that add up to target.
    Return their indices.
    """
    # Hash map: number → index
    # Why: O(1) lookup to find complement
    seen = {}
    
    # Loop through array once
    for i, num in enumerate(nums):
        # What number do we need to reach target?
        complement = target - num
        
        # Did we see this complement before?
        if complement in seen:
            # Return the indices!
            return [seen[complement], i]
        
        # Remember this number for later
        seen[num] = i
    
    # No solution found
    return []

# ── Test cases ────────────────────────────
print("Test 1:")
nums = [2, 7, 11, 15]
target = 9
print(f"Input: {nums}, Target: {target}")
print(f"Output: {twoSum(nums, target)}")  # Expected: [0, 1]

print("\nTest 2:")
nums = [3, 2, 4]
target = 6
print(f"Input: {nums}, Target: {target}")
print(f"Output: {twoSum(nums, target)}")  # Expected: [1, 2]

print("\nTest 3:")
nums = [3, 3]
target = 6
print(f"Input: {nums}, Target: {target}")
print(f"Output: {twoSum(nums, target)}")  # Expected: [0, 1] (same number, different indices)

print("\nTest 4 (Edge case):")
nums = [1, 2, 3]
target = 10
print(f"Input: {nums}, Target: {target}")
print(f"Output: {twoSum(nums, target)}")  # Expected: [] (no solution)
