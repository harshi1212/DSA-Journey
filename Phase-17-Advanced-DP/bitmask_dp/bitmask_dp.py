"""
Bitmask DP
Problems with subsets or permutations of small elements
"""

def tsp_bitmask_dp(dist):
    """
    Traveling Salesman Problem using bitmask DP.
    Find shortest tour visiting all cities exactly once.
    
    dp[mask][i] = shortest path visiting cities in mask, ending at city i
    """
    n = len(dist)
    INF = float('inf')
    
    # dp[mask][i] = min distance
    dp = [[INF] * n for _ in range(1 << n)]
    
    # Start from city 0
    dp[1][0] = 0
    
    # Iterate through all subsets
    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            
            # Try going to unvisited city v
            for v in range(n):
                if mask & (1 << v) == 0:  # v not visited
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
    
    # Find min cost to visit all cities and return to 0
    full_mask = (1 << n) - 1
    result = INF
    for i in range(1, n):
        result = min(result, dp[full_mask][i] + dist[i][0])
    
    return result

def assignTasks(tasks, workers):
    """
    Assign tasks to workers to minimize total time.
    Each worker can do subset of tasks.
    
    dp[mask][w] = min time for tasks in mask using first w workers
    """
    n_tasks = len(tasks)
    n_workers = len(workers)
    INF = float('inf')
    
    # For each task subset, calculate time for one worker
    task_time = [0] * (1 << n_tasks)
    for mask in range(1 << n_tasks):
        time = 0
        for i in range(n_tasks):
            if mask & (1 << i):
                time += tasks[i]
        task_time[mask] = time
    
    # dp[mask][w] = min time for tasks in mask using first w workers
    dp = [[INF] * (n_workers + 1) for _ in range(1 << n_tasks)]
    dp[0][0] = 0
    
    for w in range(n_workers):
        for mask in range(1 << n_tasks):
            if dp[mask][w] == INF:
                continue
            
            # Assign subset of remaining tasks to worker w
            remaining = ((1 << n_tasks) - 1) ^ mask
            submask = remaining
            
            while submask > 0:
                new_mask = mask | submask
                dp[new_mask][w+1] = min(dp[new_mask][w+1], 
                                       max(dp[mask][w], task_time[submask]))
                submask = (submask - 1) & remaining
    
    return dp[(1 << n_tasks) - 1][n_workers]

# Example 1: TSP
print("=== Bitmask DP: Traveling Salesman ===\n")

# Distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

print("Distance matrix (cities 0-3):")
for row in dist:
    print(f"  {row}")

result = tsp_bitmask_dp(dist)
print(f"\nShortest tour: {result}")

# Example 2: Task Assignment
print("\n=== Bitmask DP: Task Assignment ===\n")

tasks = [2, 3, 1, 4]  # Task durations
workers = 2

print(f"Tasks: {tasks} (durations)")
print(f"Workers: {workers}")

result = assignTasks(tasks, workers)
print(f"\nMinimum time to complete all: {result}")
print(f"(Load balancing: minimize max time any worker takes)")

# Example 3: Explanation of bitmask
print("\n=== Bitmask Explanation ===\n")

mask_example = 0b1011  # Binary
print(f"Bitmask: {bin(mask_example)}")
print("Represents subset of cities:")
for i in range(4):
    if mask_example & (1 << i):
        print(f"  City {i} is in subset")

print("\n=== Bitmask DP Complexity ===")
print("States:  O(2^n * n) - 2^n subsets, n ending positions")
print("Transition: O(n) or O(2^n) depending on problem")
print("Total: O(2^n * n²) typical")
print("\nLimited to n ≤ 20 (2^20 = ~1M)")
print("\nUse when: n small, need to consider all subsets")
