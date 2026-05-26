"""
TEMPLATE: Binary Search
Use for: Sorted arrays, decision problems
Complexity: O(log n)
"""

def binary_search(arr, target):
    """Find exact target"""
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

def binary_search_leftmost(arr, target):
    """Find leftmost position of target"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left if left < len(arr) and arr[left] == target else -1

def binary_search_rightmost(arr, target):
    """Find rightmost position of target"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1 if left > 0 and arr[left - 1] == target else -1

def binary_search_min_in_rotated(arr):
    """Find minimum in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]

# Usage:
print("Template 2: Binary Search")

arr = [1, 3, 3, 3, 5, 7, 9]
print(f"Find 3: {binary_search(arr, 3)}")
print(f"Leftmost 3: {binary_search_leftmost(arr, 3)}")
print(f"Rightmost 3: {binary_search_rightmost(arr, 3)}")

rotated = [4, 5, 6, 7, 0, 1, 2]
print(f"Min in rotated: {binary_search_min_in_rotated(rotated)}")
