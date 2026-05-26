# Sorting Algorithms

print("=== SORTING ALGORITHMS ===\n")

# ── Bubble Sort ────────────────────────────
# Why: Simple but slow, O(n²)
def bubble_sort(arr):
    """
    Repeatedly swap adjacent elements if out of order.
    """
    n = len(arr)
    
    # Each pass puts one element in correct place
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Compare and swap if out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

print("Bubble Sort:")
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
print(f"Sorted:   {bubble_sort(arr.copy())}")

# ── Merge Sort ────────────────────────────
# Why: Fast O(n log n), divide and conquer
def merge_sort(arr):
    """
    Divide array in half, sort each, then merge.
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    # Compare and add smaller elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("\nMerge Sort:")
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
print(f"Sorted:   {merge_sort(arr.copy())}")

# ── Quick Sort ────────────────────────────
# Why: Fast O(n log n) average, in-place
def quick_sort(arr):
    """
    Choose pivot, partition around it, sort partitions.
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (using first element)
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + [pivot] + quick_sort(right)

print("\nQuick Sort:")
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")
print(f"Sorted:   {quick_sort(arr.copy())}")

# ── Complexity Comparison ────────────────────────────
print("\n" + "="*50)
print("SORTING COMPLEXITY")
print("="*50)
print(f"{'Algorithm':<15} {'Time':<20} {'Space':<15} {'Stable':<10}")
print("-"*60)
print(f"{'Bubble Sort':<15} {'O(n²)':<20} {'O(1)':<15} {'Yes':<10}")
print(f"{'Merge Sort':<15} {'O(n log n)':<20} {'O(n)':<15} {'Yes':<10}")
print(f"{'Quick Sort':<15} {'O(n log n) avg':<20} {'O(log n)':<15} {'No':<10}")
print(f"{'Python sort':<15} {'O(n log n)':<20} {'O(n)':<15} {'Yes':<10}")
