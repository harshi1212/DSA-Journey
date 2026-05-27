# Dynamic Programming Pattern

print("=== DYNAMIC PROGRAMMING ===\n")

print("""
WHAT: Break problem into overlapping subproblems, memoize results
WHY: Avoid recalculating same thing multiple times
WHEN: Overlapping subproblems + optimal substructure

TYPES:
1. Top-down (Memoization): Recursion + cache
2. Bottom-up (Tabulation): Iterative + table

CLASSIC PROBLEMS:
- Fibonacci: F(n) = F(n-1) + F(n-2)
- Climbing stairs: Ways to reach step n
- Coin change: Minimum coins to make amount
""")

# Example 1: Climbing Stairs
# How many ways to climb n stairs (1 or 2 steps at a time)
def climbStairs(n):
    """
    Dynamic programming bottom-up.
    dp[i] = ways to reach stair i
    """
    if n <= 1:
        return 1
    
    # dp[i] = dp[i-1] + dp[i-2]
    # (reach from 1-step or 2-step before)
    dp = [0] * (n + 1)
    dp[0] = 1  # One way to be at start
    dp[1] = 1  # One way to climb 1 stair
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print("Example: Climbing Stairs")
for n in range(1, 6):
    print(f"  n={n}: {climbStairs(n)} ways")

# Example 2: Coin Change
def coinChange(coins, amount):
    """
    Minimum coins to make amount.
    dp[i] = minimum coins to make amount i
    """
    # Initialize with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins to make 0
    
    for i in range(1, amount + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Take coin, need coin_change(amount-coin)
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

print("\nExample: Coin Change (coins=[1,2,5], amount=5)")
coins = [1, 2, 5]
amount = 5
result = coinChange(coins, amount)
print(f"  Minimum coins: {result}")  # 1 (one 5-coin)

# Example 3: House Robber
def rob(houses):
    """
    Maximum money robbing houses (can't rob adjacent).
    """
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    # dp[i] = max money robbing houses 0 to i
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    
    for i in range(2, len(houses)):
        # Rob i, or don't rob i
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
    
    return dp[-1]

print("\nExample: House Robber")
houses = [1, 2, 3, 1]
print(f"  Houses: {houses}")
print(f"  Max money: {rob(houses)}")  # 4 (rob houses 0 and 2: 1+3)
