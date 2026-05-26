"""
Problem: Kth Largest Element in an Array
Platform: LeetCode #215
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

My thought process:
  Step 1 — Input and output: Array of integers, k.
           Find kth largest element.
  Step 2 — Brute force: Sort array and get element at index n-k.
  Step 3 — Why brute force is slow: Sorting is O(n log n).
  Step 4 — Optimised approach: Use min heap of size k.
           Top of heap is kth largest.
           Can also use quickselect for O(n) average.
  Step 5 — Edge cases: k > array length? k = 1?

Approach: Min heap of size k
Time complexity:  O(n log k) — each insertion is O(log k)
Space complexity: O(k) — heap stores k elements
"""

import heapq

def findKthLargest(nums, k):
    """
    Find kth largest element using min heap.
    """
    # Min heap of size k
    # Why: Top of min heap is smallest in heap = kth largest overall
    heap = []
    
    for num in nums:
        # Add num to heap
        heapq.heappush(heap, num)
        
        # Keep heap size <= k
        # Why: Once we have k elements, the smallest is the kth largest
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Top of heap is the kth largest element
    return heap[0]

# Alternative: Using quickselect (O(n) average, not shown here)

# ── Test cases ────────────────────────────

print("Test 1:")
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Input: nums={nums}, k={k}")
print(f"Output: {findKthLargest(nums, k)}")  # Expected: 5

print("\nTest 2:")
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(f"Input: nums={nums}, k={k}")
print(f"Output: {findKthLargest(nums, k)}")  # Expected: 4

print("\nTest 3 (Single element):")
nums = [1]
k = 1
print(f"Input: nums={nums}, k={k}")
print(f"Output: {findKthLargest(nums, k)}")  # Expected: 1

print("\nTest 4 (Large k):")
nums = [3, 2, 1]
k = 1
print(f"Input: nums={nums}, k={k}")
print(f"Output: {findKthLargest(nums, k)}")  # Expected: 3 (largest)
