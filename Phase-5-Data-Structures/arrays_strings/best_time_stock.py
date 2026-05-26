"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode #121
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

My thought process:
  Step 1 — Input and output: Array of prices. 
           Find max profit by buying once and selling once.
  Step 2 — Brute force: Check every buy-sell pair.
  Step 3 — Why brute force is slow: O(n²) - check all pairs.
  Step 4 — Optimised approach: Track minimum price seen so far.
           For each price, calculate profit if we sell at this price.
  Step 5 — Edge cases: Array with 1 element? Decreasing prices?

Approach: Single pass, track min price and max profit
Time complexity:  O(n) — one pass through array
Space complexity: O(1) — only a few variables
"""

def maxProfit(prices):
    """
    Find maximum profit from buying and selling stock once.
    Must buy before sell.
    """
    # Edge case
    if not prices or len(prices) < 2:
        return 0
    
    # Track minimum price seen so far
    # Why: We can buy at any previous price
    min_price = prices[0]
    
    # Track maximum profit found so far
    max_profit = 0
    
    # Loop through prices (starting from second day)
    for price in prices[1:]:
        # If we sell at current price, what's the profit?
        potential_profit = price - min_price
        
        # Is this better than best profit so far?
        max_profit = max(max_profit, potential_profit)
        
        # Is current price lower than minimum seen?
        min_price = min(min_price, price)
    
    return max_profit

# ── Test cases ────────────────────────────
print("Test 1:")
prices = [7, 1, 5, 3, 6, 4]
print(f"Input: {prices}")
print(f"Output: {maxProfit(prices)}")  # Expected: 5 (buy at 1, sell at 6)

print("\nTest 2:")
prices = [7, 6, 4, 3, 1]
print(f"Input: {prices}")
print(f"Output: {maxProfit(prices)}")  # Expected: 0 (prices only decrease)

print("\nTest 3:")
prices = [2, 4, 1, 7, 5, 11]
print(f"Input: {prices}")
print(f"Output: {maxProfit(prices)}")  # Expected: 10 (buy at 1, sell at 11)

print("\nTest 4 (Edge case):")
prices = [1]
print(f"Input: {prices}")
print(f"Output: {maxProfit(prices)}")  # Expected: 0 (can't buy and sell with 1 price)
