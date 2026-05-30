# Dynamic Programming

## What is it?
DP = recursion + memory.
Solve a big problem by solving smaller 
subproblems — but store the answers so 
you never solve the same subproblem twice.

Think of it like this:
Fibonacci without DP: fib(5) calculates 
fib(3) multiple times — wasteful.
Fibonacci with DP: calculate fib(3) once,
store it, reuse it — fast.

## Two approaches

### Top-down (Memoization)
Write it as recursion.
Add a dictionary to store results.
If already solved — return stored answer.

### Bottom-up (Tabulation)
Build the answer from smallest subproblem up.
Use an array. No recursion needed.
Usually faster in practice.

## How to recognize a DP problem
Ask yourself:
- Does this problem have overlapping subproblems?
- Does the optimal solution use optimal 
  solutions of subproblems?
If both yes → DP.

## The DP template
Step 1: Define what dp[i] means
Step 2: Write the base case
Step 3: Write the recurrence relation
Step 4: Fill the table in correct order

## Common mistake
Jumping to DP without first writing 
the brute force recursive solution.
Always start with recursion, then add memo.

## Practice problems
- Easy: Climbing Stairs (LeetCode #70)
- Medium: Coin Change (LeetCode #322)
- Hard: Longest Increasing Subsequence (#300)
