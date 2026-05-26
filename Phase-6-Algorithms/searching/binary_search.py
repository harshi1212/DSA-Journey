"""
Binary Search Algorithm
Difficulty: Medium

Search for target in SORTED array in O(log n) time.
"""

def binary_search(arr, target):
    """
    Search for target using binary search.
    Array must be SORTED.
    Returns index of target, or -1 if not found.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Find middle point
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # Target is in right half, ignore left
            left = mid + 1
        else:
            # Target is in left half, ignore right
            right = mid - 1
    
    return -1

print("Binary Search Examples:")
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Array: {arr}")
print(f"Search 7: {binary_search(arr, 7)}")      # 3
print(f"Search 13: {binary_search(arr, 13)}")    # 6
print(f"Search 10: {binary_search(arr, 10)}")    # -1 (not found)
