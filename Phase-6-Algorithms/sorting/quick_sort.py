"""
Quick Sort - Partition based sorting
Time: O(n log n) average, Space: O(log n)
"""

def quick_sort(arr):
    """Sort using quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print("Quick Sort:")
arr = [3, 6, 8, 10, 1, 2, 1]
print(f"Original: {arr}")
print(f"Sorted:   {quick_sort(arr)}")
