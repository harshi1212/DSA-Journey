"""
Problem: 3Sum
Platform: LeetCode #15
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

My thought process:
  Step 1 — Input and output: Array of integers.
           Find all unique triplets that sum to 0.
  Step 2 — Brute force: Check all triplets (nested 3 loops).
  Step 3 — Why brute force is slow: O(n³) - triple nested loops.
  Step 4 — Optimised approach: Sort array, then for each element,
           use two pointers to find pair that sums to -element.
  Step 5 — Edge cases: Duplicates, negative numbers, all zeros?

Approach: Sort array, fix one element, use two pointers for rest
Time complexity:  O(n²) — sorting O(n log n), then O(n²) for two pointers
Space complexity: O(1) or O(n) depending on if we count output
"""

def threeSum(nums):
    """
    Find all unique triplets in array that sum to 0.
    Return list of triplets (no duplicates).
    """
    # Edge case
    if not nums or len(nums) < 3:
        return []
    
    # Sort array first
    # Why: Allows two pointer technique, helps skip duplicates
    nums.sort()
    
    result = []
    n = len(nums)
    
    # Fix one number at a time
    for i in range(n - 2):
        current = nums[i]
        
        # If current is positive, no triplet can sum to 0
        # Why: All remaining numbers are also positive
        if current > 0:
            break
        
        # Skip duplicate values to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Find two numbers that sum to -current (using two pointers)
        left = i + 1
        right = n - 1
        target = -current
        
        while left < right:
            total = nums[left] + nums[right]
            
            if total == target:
                # Found a triplet!
                result.append([current, nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif total < target:
                # Need larger sum, move left pointer right
                left += 1
            
            else:
                # Need smaller sum, move right pointer left
                right -= 1
    
    return result

# ── Test cases ────────────────────────────
print("Test 1:")
nums = [-1, 0, 1, 2, -1, -4]
print(f"Input: {nums}")
result = threeSum(nums)
print(f"Output: {result}")  # Expected: [[-1, -1, 2], [-1, 0, 1]]

print("\nTest 2:")
nums = [0, 0, 0, 0]
print(f"Input: {nums}")
result = threeSum(nums)
print(f"Output: {result}")  # Expected: [[0, 0, 0]]

print("\nTest 3:")
nums = [-2, 0, 1, 1, 2]
print(f"Input: {nums}")
result = threeSum(nums)
print(f"Output: {result}")  # Expected: [[-2, 0, 2], [-2, 1, 1]]

print("\nTest 4 (Edge case):")
nums = [0, 0]
print(f"Input: {nums}")
result = threeSum(nums)
print(f"Output: {result}")  # Expected: [] (less than 3 elements)
