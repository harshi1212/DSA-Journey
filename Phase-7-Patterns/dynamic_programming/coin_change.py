"""
DP Example: Coin Change
Minimum number of coins to make target amount.
"""

def coinChange(coins, amount):
    """Find minimum coins to make amount."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

print("Coin Change:")
coins = [1, 2, 5]
amount = 5
print(f"coins={coins}, amount={amount}: {coinChange(coins, amount)}")  # 1

coins = [2]
amount = 3
print(f"coins={coins}, amount={amount}: {coinChange(coins, amount)}")  # -1
