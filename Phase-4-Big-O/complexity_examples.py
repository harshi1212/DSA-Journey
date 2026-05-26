"""
TOPIC: Complexity Analysis Examples
Difficulty: Beginner-Intermediate

Measure how fast/efficient code is as input grows.
"""

import time

print("=== COMPLEXITY ANALYSIS ===\n")

# ── O(1) - Constant Time ────────────────────────────
# Why: Doesn't depend on input size
def get_first_element(arr):
    return arr[0]  # Always takes same time

# ── O(n) - Linear Time ────────────────────────────
# Why: Goes through each element once
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# ── O(n²) - Quadratic Time ────────────────────────────
# Why: Nested loops (loop inside loop)
def bubble_sort_simple(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ── O(log n) - Logarithmic Time ────────────────────────────
# Why: Halve the problem each time (binary search)
def binary_search(arr, target):
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

# ── O(n log n) - Linearithmic Time ────────────────────────────
# Why: Each element processes log(n) times
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Complexity Comparison:")
print("-" * 50)

# Compare different complexities
test_sizes = [10, 100, 1000, 10000]

for n in test_sizes:
    o_1 = 1
    o_n = n
    o_n2 = n * n
    o_log_n = n * ((len(str(n))-1).bit_length())  # Approximate log(n)
    o_n_log_n = n * ((len(str(n))-1).bit_length())
    
    print(f"\nInput size n = {n}")
    print(f"  O(1)       ≈ {o_1:>15,} operations")
    print(f"  O(log n)   ≈ {o_log_n:>15,} operations")
    print(f"  O(n)       ≈ {o_n:>15,} operations")
    print(f"  O(n log n) ≈ {o_n_log_n:>15,} operations")
    print(f"  O(n²)      ≈ {o_n2:>15,} operations")

print("\n" + "="*50)
print("KEY INSIGHT: As n grows, O(n²) becomes MUCH slower than O(n)")
print("="*50)

# Space Complexity Examples
print("\n=== SPACE COMPLEXITY ===\n")

# O(1) - Constant space
def sum_array_o1(arr):
    total = 0  # Only one variable
    for num in arr:
        total += num
    return total

# O(n) - Linear space
def double_array_on(arr):
    result = []  # Creates new array of size n
    for num in arr:
        result.append(num * 2)
    return result

# O(n) - Space for recursion
def fibonacci_on(n):
    if n <= 1:
        return n
    return fibonacci_on(n - 1) + fibonacci_on(n - 2)  # Call stack grows

# O(n) - Using recursion with stack
def count_to_n(n):
    if n == 0:
        return
    print(n)
    count_to_n(n - 1)  # Stack grows n levels

print("Space Complexity Types:")
print("- O(1): Only a few variables, no matter input size")
print("- O(n): Create array/list of same size as input")
print("- O(n): Recursion depth = input size")

# Practical Example: Time Analysis
print("\n" + "="*50)
print("PRACTICAL TIMING EXAMPLE")
print("="*50)

arr = list(range(1000))  # Array of 1000 numbers

# O(n) - Linear
start = time.time()
for i in range(10000):
    find_max(arr)
linear_time = time.time() - start
print(f"\nO(n) solution (10,000 iterations): {linear_time:.4f} seconds")

# O(n²) - Much slower for same input
arr_small = list(range(100))  # Smaller array because O(n²) is slow
start = time.time()
for i in range(100):
    bubble_sort_simple(arr_small.copy())
quadratic_time = time.time() - start
print(f"O(n²) solution (100 iterations): {quadratic_time:.4f} seconds")

print("\n⚠️  Even with smaller array and fewer iterations,")
print("    O(n²) takes MUCH longer than O(n)")
