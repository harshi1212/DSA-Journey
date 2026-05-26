# Sliding Window Pattern - Notes

print("=== SLIDING WINDOW TECHNIQUE ===\n")

print("""
WHAT IS IT:
A window (contiguous subarray) that slides across the array.
Two types:
1. Fixed size: window size never changes
2. Dynamic: window size changes based on condition

WHY USE IT:
Convert nested loops (O(n²)) into single loop (O(n))

HOW IT WORKS:
1. Define window boundaries (left, right)
2. Expand window by moving right pointer
3. When condition violated, shrink by moving left pointer
4. Track answer as window changes

WHEN TO USE:
- Contiguous subarray problems
- String substring problems
- Sliding window maximums/minimums
- Fixed or variable window sizes
""")

print("EXAMPLE: Fixed-Size Window")
print("-" * 50)

# Example: Maximum sum subarray of size k
def maxSumSubarray(arr, k):
    """Find maximum sum of any subarray of size k."""
    # Calculate initial window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide: remove left, add right
    for i in range(1, len(arr) - k + 1):
        window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(f"Array: {arr}")
print(f"Window size: {k}")
print(f"Max sum: {maxSumSubarray(arr, k)}")  # 24 (10+2+3+1+0+20 = 36, wait...)

# Let me fix this - show windows
print("\nWindows:")
for i in range(len(arr) - k + 1):
    window = arr[i:i+k]
    print(f"  {window} → sum = {sum(window)}")
