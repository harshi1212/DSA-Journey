"""
TEMPLATE: Dynamic Programming
Use for: Optimization, counting, decision problems
Complexity: Varies (usually O(n²) or O(n*m))
"""

# Knapsack 0/1
def knapsack_01(weights, values, capacity):
    """Classic 0/1 knapsack"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Longest Increasing Subsequence
def lis(arr):
    """LIS with binary search - O(n log n)"""
    import bisect
    
    tails = []
    
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

# Longest Common Subsequence
def lcs(text1, text2):
    """LCS length"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Coin Change
def coin_change(coins, amount):
    """Minimum coins to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Usage:
print("Template 5: Dynamic Programming")

print(f"Knapsack: {knapsack_01([2, 3, 4], [3, 4, 5], 5)}")
print(f"LIS: {lis([10, 9, 2, 5, 3, 7, 101, 18])}")
print(f"LCS: {lcs('abc', 'ac')}")
print(f"Coin Change: {coin_change([1, 2, 5], 5)}")
