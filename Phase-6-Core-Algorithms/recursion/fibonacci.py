"""
TOPIC: Fibonacci and Dynamic Programming Intro
Difficulty: Beginner-Intermediate

Fibonacci optimized using memoization and DP.
"""

print("=== FIBONACCI OPTIMIZATION ===\n")

# Version 1: Naive recursion (SLOW)
# Why: Recalculates same values many times
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

print("Version 1: Naive Recursion")
print(f"fib(5) = {fib_naive(5)}")  # 5
# print(f"fib(40) = {fib_naive(40)}")  # TIMEOUT! Don't run this

# Version 2: Memoization (FAST)
# Why: Store results, never recalculate
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    # If already calculated, return it
    if n in memo:
        return memo[n]
    
    # Base case
    if n <= 1:
        return n
    
    # Calculate and store
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print("\nVersion 2: Memoization (Top-Down DP)")
print(f"fib(5) = {fib_memo(5)}")    # 5
print(f"fib(30) = {fib_memo(30)}")  # 832040 (fast!)
print(f"fib(50) = {fib_memo(50)}")  # Very fast

# Version 3: Tabulation (ALSO FAST)
# Why: Build solution from bottom up
def fib_tab(n):
    # Create array to store results
    dp = [0] * (n + 1)
    
    # Base cases
    if n >= 1:
        dp[1] = 1
    
    # Fill array from bottom to top
    for i in range(2, n + 1):
        # F(i) = F(i-1) + F(i-2)
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print("\nVersion 3: Tabulation (Bottom-Up DP)")
print(f"fib(5) = {fib_tab(5)}")    # 5
print(f"fib(30) = {fib_tab(30)}")  # 832040
print(f"fib(100) = {fib_tab(100)}")  # Huge number, very fast

# Version 4: Space-Optimized
# Why: Don't need entire array, just last 2 values
def fib_optimized(n):
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

print("\nVersion 4: Space-Optimized (O(1) space)")
print(f"fib(5) = {fib_optimized(5)}")    # 5
print(f"fib(50) = {fib_optimized(50)}")  # Very fast, minimal memory

# Comparison
print("\n" + "="*50)
print("COMPLEXITY COMPARISON")
print("="*50)
print(f"{'Method':<20} {'Time':<15} {'Space':<15}")
print("-"*50)
print(f"{'Naive':<20} {'O(2^n)':<15} {'O(n)':<15}")
print(f"{'Memoization':<20} {'O(n)':<15} {'O(n)':<15}")
print(f"{'Tabulation':<20} {'O(n)':<15} {'O(n)':<15}")
print(f"{'Space-Optimized':<20} {'O(n)':<15} {'O(1)':<15}")
