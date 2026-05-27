# Backtracking Pattern

print("=== BACKTRACKING PATTERN ===\n")

print("""
WHAT: Explore all possibilities, mark/unmark choices
WHY: Find all solutions, combinations, permutations
WHEN: Choice problems with multiple answers

TECHNIQUE:
1. Choose: Add choice
2. Explore: Recurse with choice
3. Unchoose: Remove choice (backtrack)

PROBLEMS:
- Subsets: All subsets of array
- Permutations: All orderings
- Combinations: All combinations
- N-Queens: Place queens without conflict
""")

# Example 1: Subsets
def subsets(nums):
    """Find all subsets of nums."""
    result = []
    
    def backtrack(index, current):
        # Add current subset to result
        result.append(current[:])
        
        # Try adding each remaining number
        for i in range(index, len(nums)):
            # Choose
            current.append(nums[i])
            # Explore
            backtrack(i + 1, current)
            # Unchoose
            current.pop()
    
    backtrack(0, [])
    return result

print("Example: Subsets of [1,2,3]")
result = subsets([1, 2, 3])
for subset in result:
    print(f"  {subset}")

# Example 2: Permutations
def permutations(nums):
    """Find all permutations of nums."""
    result = []
    
    def backtrack(current):
        # If all numbers used, add permutation
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        # Try each unused number
        for num in nums:
            if num not in current:
                # Choose
                current.append(num)
                # Explore
                backtrack(current)
                # Unchoose
                current.pop()
    
    backtrack([])
    return result

print("\nExample: Permutations of [1,2,3]")
result = permutations([1, 2, 3])
print(f"Total: {len(result)} permutations")
for perm in result[:3]:  # Show first 3
    print(f"  {perm}")
print("  ...")

# Example 3: Combinations
def combinations(n, k):
    """Find all combinations of k numbers from 1 to n."""
    result = []
    
    def backtrack(start, current):
        # If got k numbers, add combination
        if len(current) == k:
            result.append(current[:])
            return
        
        # Try numbers from start to n
        for i in range(start, n + 1):
            # Choose
            current.append(i)
            # Explore: next start is i+1
            backtrack(i + 1, current)
            # Unchoose
            current.pop()
    
    backtrack(1, [])
    return result

print("\nExample: Combinations C(4,2)")
result = combinations(4, 2)
for comb in result:
    print(f"  {comb}")
