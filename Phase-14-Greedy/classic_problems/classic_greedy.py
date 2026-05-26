"""
Classic Greedy Problems: Gas Station, Candy, Jump Game, Coin Change
"""

# ─────────────────────────────────────────────────────────────────
# Problem 1: Gas Station (LeetCode 134)
# ─────────────────────────────────────────────────────────────────

def canCompleteCircuit(gas, cost):
    """
    Greedy insight: If total gas >= total cost, solution exists.
    We need to find starting position.
    
    Greedy choice: If can't reach i from j, can't reach i from j-1 either.
    """
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    # No solution if not enough gas
    if total_gas < total_cost:
        return -1
    
    # Find starting position
    tank = 0
    start = 0
    
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        
        # If tank becomes negative, start is not here
        if tank < 0:
            tank = 0
            start = i + 1
    
    return start

print("=== Problem 1: Gas Station ===\n")
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(f"Gas: {gas}")
print(f"Cost: {cost}")
print(f"Starting position: {canCompleteCircuit(gas, cost)}")  # 3

# ─────────────────────────────────────────────────────────────────
# Problem 2: Candy Distribution (LeetCode 135)
# ─────────────────────────────────────────────────────────────────

def distributeCandies(ratings):
    """
    Each child gets at least 1 candy.
    If child i has higher rating than neighbor, gets more candy.
    Find minimum total candies.
    
    Greedy: Two passes (left-to-right, right-to-left).
    """
    n = len(ratings)
    candies = [1] * n
    
    # Left to right: if rating increases, increase candies
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Right to left: if rating increases (going backwards), ensure enough
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

print("\n=== Problem 2: Candy Distribution ===\n")
ratings = [1, 0, 2]
print(f"Ratings: {ratings}")
print(f"Minimum candies: {distributeCandies(ratings)}")  # 5

# ─────────────────────────────────────────────────────────────────
# Problem 3: Jump Game (LeetCode 55)
# ─────────────────────────────────────────────────────────────────

def canJump(nums):
    """
    Given array of jump heights, can reach the last index?
    
    Greedy insight: Track maximum reachable position.
    If current index > max reachable, can't proceed.
    """
    max_reach = 0
    
    for i in range(len(nums)):
        # If can't reach here, stop
        if i > max_reach:
            return False
        
        # Update max reachable from here
        max_reach = max(max_reach, i + nums[i])
        
        # Optimization: if can reach end, done
        if max_reach >= len(nums) - 1:
            return True
    
    return False

print("\n=== Problem 3: Jump Game ===\n")
print(f"[2,3,1,1,4]: {canJump([2, 3, 1, 1, 4])}")  # True
print(f"[3,2,1,0,4]: {canJump([3, 2, 1, 0, 4])}")  # False

# ─────────────────────────────────────────────────────────────────
# Problem 4: Min Coins (Classic DP, but greedy works for certain coins)
# ─────────────────────────────────────────────────────────────────

def minCoinsGreedy(coins, amount):
    """
    Greedy approach (only works for certain coin systems like USD).
    For arbitrary coins, use DP!
    
    Example where greedy FAILS:
      coins = [1, 3, 4], amount = 6
      Greedy: 4 + 1 + 1 = 3 coins
      Optimal: 3 + 3 = 2 coins
    """
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        count += amount // coin
        amount %= coin
    
    return count

print("\n=== Problem 4: Min Coins (Greedy - CAREFUL!) ===\n")
print("USD coins [1, 5, 10, 25] for amount 41:")
coins_usd = [1, 5, 10, 25]
coins_usd.sort(reverse=True)
amount = 41
count = 0
for coin in coins_usd:
    use = amount // coin
    if use > 0:
        print(f"  {use} x {coin}c coin")
    count += use
    amount %= coin
print(f"Total: {count} coins")

print("\nBut greedy FAILS on [1,3,4] for amount 6:")
print("  Greedy: 4 + 1 + 1 = 3 coins")
print("  Optimal: 3 + 3 = 2 coins")
print("  Use DP for arbitrary coin systems!")

print("\n=== Complexity ===")
print("Gas Station: O(n)")
print("Candy:       O(n)")
print("Jump Game:   O(n)")
print("All greedy = linear time!")
