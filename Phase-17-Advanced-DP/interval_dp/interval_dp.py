"""
Interval DP
Problems involving ranges/substrings
"""

# ─────────────────────────────────────────────────────────────────
# Example 1: Burst Balloons (LeetCode 312)
# ─────────────────────────────────────────────────────────────────

def burstBalloons(nums):
    """
    Burst balloons to maximize coins.
    Coins = left * balloon * right when burst.
    
    Key insight: Think backward - what was burst LAST?
    """
    # Add sentinel 1s
    nums = [1] + nums + [1]
    n = len(nums)
    
    # dp[i][j] = max coins burst from balloon i to j (exclusive ends)
    dp = [[0] * n for _ in range(n)]
    
    # Length of interval (2 to n-1 because of sentinels)
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            # Try bursting each balloon k last (between i and j)
            for k in range(i + 1, j):
                # If k is burst last: nums[i] * nums[k] * nums[j]
                # Plus coins from bursting i to k, and k to j
                dp[i][j] = max(dp[i][j], dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j])
    
    return dp[0][n-1]

print("=== Advanced DP: Interval DP ===\n")
print("Example 1: Burst Balloons\n")

nums = [3, 1, 5, 8]
result = burstBalloons(nums)
print(f"Balloons: {nums}")
print(f"Maximum coins: {result}")

# ─────────────────────────────────────────────────────────────────
# Example 2: Matrix Chain Multiplication
# ─────────────────────────────────────────────────────────────────

def matrixChainOrder(p):
    """
    Find order of matrix multiplication to minimize scalar multiplications.
    p[i-1] x p[i] is dimension of matrix i.
    """
    n = len(p) - 1
    
    # dp[i][j] = min multiplications for matrices i to j
    dp = [[0] * n for _ in range(n)]
    
    # Length of chain
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # Try split point
            for k in range(i, j):
                # Cost = left chain + right chain + multiply results
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]

print("\n=== Example 2: Matrix Chain ===\n")

# Matrices: 10x30, 30x5, 5x60
p = [10, 30, 5, 60]

result = matrixChainOrder(p)
print(f"Matrix dimensions: 10x30, 30x5, 5x60")
print(f"Minimum multiplications: {result}")
print(f"\nOptimal: (A * B) * C = 10*30*5 + 10*5*60 = 1500 + 3000 = 4500")

# ─────────────────────────────────────────────────────────────────
# Example 3: Palindrome Partitioning
# ─────────────────────────────────────────────────────────────────

def minCut(s):
    """Minimum cuts needed to partition string into palindromes."""
    n = len(s)
    
    # is_palin[i][j] = true if s[i:j+1] is palindrome
    is_palin = [[False] * n for _ in range(n)]
    
    # Build palindrome table
    for i in range(n):
        is_palin[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or is_palin[i+1][j-1]):
                is_palin[i][j] = True
    
    # dp[i] = min cuts for s[0:i+1]
    dp = [0] * n
    
    for i in range(n):
        if is_palin[0][i]:
            dp[i] = 0  # Whole string is palindrome
        else:
            dp[i] = i  # Worst case: i cuts
            for j in range(i):
                if is_palin[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n-1]

print("\n=== Example 3: Palindrome Partitioning ===\n")

test_strings = ["nitin", "geeks", "aab"]

for s in test_strings:
    cuts = minCut(s)
    print(f"'{s}': minimum cuts = {cuts}")

print("\n=== Interval DP Complexity ===")
print("State:  O(n²) - all pairs (i, j)")
print("Transition: O(n) - try all split points k")
print("Total: O(n³)")
print("\nUse when: Problem involves contiguous ranges")
