"""
TOPIC: Recursion
Difficulty: Beginner-Intermediate

Recursion: Function calling itself.
Base case: When to stop. Recursive case: How to break down.
"""

print("=== RECURSION ===\n")

# ── Example 1: Factorial ────────────────────────────
# Why: Simple recursion example
def factorial(n):
    """
    Calculate n! = n × (n-1) × (n-2) × ... × 1
    """
    # Base case: stop here
    if n <= 1:
        return 1
    
    # Recursive case: break problem into smaller pieces
    # Why: 5! = 5 × 4!
    return n * factorial(n - 1)

print("Factorial:")
print(f"5! = {factorial(5)}")  # 120
print(f"3! = {factorial(3)}")  # 6

# ── Example 2: Fibonacci ────────────────────────────
# Why: Classic recursion problem (but inefficient)
def fibonacci(n):
    """
    Calculate nth Fibonacci number.
    Series: 0, 1, 1, 2, 3, 5, 8, 13...
    """
    # Base cases
    if n <= 1:
        return n
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci (Naive - slow):")
print(f"F(5) = {fibonacci(5)}")   # 5
print(f"F(6) = {fibonacci(6)}")   # 8

# Optimized fibonacci using memoization
# Why: Remember previously calculated values
def fibonacci_memo(n, memo={}):
    """Fibonacci with memoization (fast)."""
    # Check if already calculated
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 1:
        return n
    
    # Calculate and remember
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("\nFibonacci (Memoized - fast):")
print(f"F(10) = {fibonacci_memo(10)}")  # 55
print(f"F(20) = {fibonacci_memo(20)}")  # 6765

# ── Example 3: Sum of Array ────────────────────────────
def sum_array(arr):
    """
    Sum all elements in array using recursion.
    """
    # Base case: empty array
    if not arr:
        return 0
    
    # Recursive case: first element + sum of rest
    # Why: [1,2,3,4] = 1 + sum([2,3,4])
    return arr[0] + sum_array(arr[1:])

print("\nSum of Array:")
print(f"sum([1,2,3,4]) = {sum_array([1,2,3,4])}")  # 10

# ── Example 4: Binary Search (Recursive) ────────────────────────────
def binary_search_recursive(arr, target, left, right):
    """
    Search for target in sorted array using recursion.
    """
    # Base case: target not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # Recursive case: search right half
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # Recursive case: search left half
        return binary_search_recursive(arr, target, left, mid - 1)

print("\nBinary Search (Recursive):")
arr = [1, 3, 5, 7, 9, 11]
print(f"Index of 7: {binary_search_recursive(arr, 7, 0, len(arr)-1)}")  # 3
print(f"Index of 2: {binary_search_recursive(arr, 2, 0, len(arr)-1)}")  # -1

# ── Recursion Tree Visualization ────────────────────────────
print("\nRecursion Tree Example: F(4)")
print("""
           F(4)
          /    \\
       F(3)     F(2)
      /   \\     /   \\
    F(2)  F(1) F(1) F(0)
    / \\
  F(1) F(0)

Each function call is a node in the tree.
Deeper trees = more function calls = slower!
""")

# ── Common Mistakes ────────────────────────────
print("COMMON MISTAKES:")
print("1. No base case → infinite recursion")
print("2. Wrong base case → wrong answer")
print("3. Inefficient recursion → timeout (use memoization)")
print("4. Too deep recursion → stack overflow")
