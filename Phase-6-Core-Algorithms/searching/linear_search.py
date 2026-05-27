# Searching Algorithms

print("=== SEARCHING ALGORITHMS ===\n")

# ── Linear Search ────────────────────────────
# Why: Simplest, works on unsorted arrays
def linear_search(arr, target):
    """
    Search for target in array from left to right.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return -1  # Not found

print("Linear Search:")
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Array: {arr}")
print(f"Index of 5: {linear_search(arr, 5)}")  # 4
print(f"Index of 10: {linear_search(arr, 10)}")  # -1

# ── Binary Search ────────────────────────────
# Why: MUCH faster on sorted arrays, O(log n)
def binary_search(arr, target):
    """
    Search for target in SORTED array using binary search.
    Divide and conquer: eliminate half each time.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Found!
        elif arr[mid] < target:
            # Target is in right half
            left = mid + 1
        else:
            # Target is in left half
            right = mid - 1
    
    return -1  # Not found

print("\nBinary Search:")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr}")
print(f"Index of 7: {binary_search(arr, 7)}")  # 6
print(f"Index of 1: {binary_search(arr, 1)}")  # 0
print(f"Index of 10: {binary_search(arr, 10)}")  # 9
print(f"Index of 15: {binary_search(arr, 15)}")  # -1

# ── Comparison ────────────────────────────
print("\n" + "="*50)
print("Linear vs Binary Search")
print("="*50)

arr_1000 = list(range(1, 1001))

import time

# Linear search
start = time.time()
for _ in range(1000):
    linear_search(arr_1000, 500)
linear_time = time.time() - start

# Binary search
start = time.time()
for _ in range(1000):
    binary_search(arr_1000, 500)
binary_time = time.time() - start

print(f"Linear search (1000 iterations): {linear_time:.6f} seconds")
print(f"Binary search (1000 iterations): {binary_time:.6f} seconds")
print(f"Binary is {linear_time/binary_time:.1f}x faster!")
