# Phase 17 - Advanced Dynamic Programming

## Beyond Basic DP

Basic DP: `dp[i] = function of dp[i-1], dp[i-2], ...`

Advanced DP: Different state definitions for different problem structures.

---

## Master These 4 Advanced Patterns

| Pattern | State | Example | Complexity |
|---------|-------|---------|-----------|
| **Interval DP** | `dp[i][j]` = result for substring/subarray i to j | Burst balloons, matrix chain | O(n³) |
| **Bitmask DP** | `dp[mask][pos]` = result with subset `mask` | TSP, assign tasks | O(2^n * n²) |
| **Tree DP** | `dp[node][state]` = result rooted at node | Rob house on tree | O(n) |
| **Digit DP** | `dp[pos][tight][...]` = count of numbers | Count digit one | O(log max * states) |

---

## When to Use Each

**Interval DP**: Substring/subarray problems, matrix problems  
**Bitmask DP**: Small n (≤20), need subsets  
**Tree DP**: Tree structure problems  
**Digit DP**: Counting problems with digit constraints  

---

## Key Insight

Advanced DP = choosing the right **state definition** for the problem structure.

Same recurrence, different dimension!

---

## Progression

1. Basic DP: Linear state (1D or 2D arrays)
2. Interval DP: 2D range problems
3. Bitmask DP: Exponential state (small n)
4. Tree DP: Recursive structure
5. Digit DP: Mathematical constraints

Master each builds on previous!
