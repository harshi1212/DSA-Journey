"""
Backtracking: Permutations
Generate all possible orderings of a list.
"""

def permute(nums):
    """Generate all permutations of nums."""
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result

print("Permutations of [1,2,3]:")
result = permute([1, 2, 3])
for perm in result:
    print(f"  {perm}")
print(f"Total: {len(result)}")
