"""
Tree DP
Dynamic programming on tree structures
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ─────────────────────────────────────────────────────────────────
# Example 1: House Robber III - Rob houses in tree
# ─────────────────────────────────────────────────────────────────

def rob_tree(root):
    """
    Rob houses in tree, can't rob adjacent.
    
    State:
    - rob[node] = max money if rob this house
    - skip[node] = max money if skip this house
    """
    def dfs(node):
        if not node:
            return (0, 0)  # (rob, skip)
        
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        
        # If rob this node: can't rob children
        rob = node.val + left_skip + right_skip
        
        # If skip this node: can rob or skip children
        skip = max(left_rob, left_skip) + max(right_rob, right_skip)
        
        return (rob, skip)
    
    rob_val, skip_val = dfs(root)
    return max(rob_val, skip_val)

# ─────────────────────────────────────────────────────────────────
# Example 2: Maximum Path Sum in Binary Tree
# ─────────────────────────────────────────────────────────────────

def maxPathSum(root):
    """
    Find maximum path sum (can go through any node).
    Path doesn't need to start/end at root.
    """
    max_sum = [float('-inf')]
    
    def dfs(node):
        if not node:
            return 0
        
        # Get max path from left and right
        left_max = max(0, dfs(node.left))
        right_max = max(0, dfs(node.right))
        
        # Max path through this node
        path_through = node.val + left_max + right_max
        max_sum[0] = max(max_sum[0], path_through)
        
        # Return max path starting from this node
        return node.val + max(left_max, right_max)
    
    dfs(root)
    return max_sum[0]

# ─────────────────────────────────────────────────────────────────
# Example 3: Maximum Independent Set in Tree
# ─────────────────────────────────────────────────────────────────

def maxIndependentSet(root):
    """
    Maximum independent set in tree (no two adjacent nodes).
    Similar to House Robber.
    """
    def dfs(node):
        if not node:
            return (0, 0)
        
        left_include, left_exclude = dfs(node.left)
        right_include, right_exclude = dfs(node.right)
        
        # Include this node
        include = node.val + left_exclude + right_exclude
        
        # Exclude this node
        exclude = max(left_include, left_exclude) + max(right_include, right_exclude)
        
        return (include, exclude)
    
    include, exclude = dfs(root)
    return max(include, exclude)

# Build example trees
print("=== Tree DP Examples ===\n")

# Example tree:
#         3
#        / \
#       2   3
#        \
#         3

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)

print("Tree structure:")
print("       3")
print("      / \\")
print("     2   3")
print("      \\")
print("       3\n")

# Example 1: House Robber III
print("Example 1: House Robber III")
result = rob_tree(root)
print(f"Maximum money that can be robbed: {result}")
print("Explanation: Rob root (3) and bottom right (3) = 6\n")

# Example 2: Max Path Sum
print("Example 2: Maximum Path Sum")
result = maxPathSum(root)
print(f"Maximum path sum: {result}")
print("Explanation: 2 + 3 + 3 + 3 = 11 (or other paths)\n")

# Example 3: Max Independent Set
print("Example 3: Maximum Independent Set")
result = maxIndependentSet(root)
print(f"Maximum independent set size: {result}\n")

# More complex tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

print("Another tree:")
print("       1")
print("      / \\")
print("     2   3")
print("    / \\")
print("   4   5\n")

result = rob_tree(root2)
print(f"House Robber III result: {result}")

print("\n=== Tree DP Complexity ===")
print("Recurrence: For each node, combine children's results")
print("Time:  O(n) - visit each node once")
print("Space: O(h) - recursion depth, h = height")
print("\nUse when: Problem has recursive tree structure")
