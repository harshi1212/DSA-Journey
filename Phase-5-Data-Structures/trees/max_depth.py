"""
Problem: Maximum Depth of Binary Tree
Platform: LeetCode #104
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

My thought process:
  Step 1 — Input and output: Root of binary tree.
           Find maximum depth (longest path from root to leaf).
  Step 2 — Brute force: Recursively explore all paths.
  Step 3 — Why brute force: Actually efficient! Trees are made for recursion.
  Step 4 — Optimised approach: Recursion naturally solves this.
           Max depth = 1 + max(left_depth, right_depth).
  Step 5 — Edge cases: Empty tree? Single node?

Approach: Recursive depth-first search
Time complexity:  O(n) — visit each node once
Space complexity: O(h) — h = height, recursion stack depth
"""

class TreeNode:
    """Node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    Find maximum depth (height) of binary tree.
    Depth = longest path from root to leaf.
    """
    # Base case: empty tree
    if not root:
        return 0
    
    # Recursive case: 1 + max depth of subtrees
    # Why: Each node adds 1 to depth
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Maximum depth is 1 (current node) + deeper subtree
    return 1 + max(left_depth, right_depth)

# Alternative: Iterative using BFS (level-order traversal)
from collections import deque

def maxDepthIterative(root):
    """Find max depth using iteration (BFS)."""
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth

# ── Test cases ────────────────────────────

print("Test 1:")
#       3
#      / \
#     9  20
#       /  \
#      15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(f"Max depth: {maxDepth(root)}")  # Expected: 3

print("\nTest 2:")
#       2
#        \
#         3
root = TreeNode(2)
root.right = TreeNode(3)
print(f"Max depth: {maxDepth(root)}")  # Expected: 2

print("\nTest 3 (Edge case):")
# Single node
root = TreeNode(1)
print(f"Max depth: {maxDepth(root)}")  # Expected: 1

print("\nTest 4 (Empty tree):")
root = None
print(f"Max depth: {maxDepth(root)}")  # Expected: 0
