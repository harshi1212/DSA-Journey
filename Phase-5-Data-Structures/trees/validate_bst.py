"""
Problem: Validate Binary Search Tree
Platform: LeetCode #98
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

My thought process:
  Step 1 — Input and output: Root of binary tree.
           Check if it's a valid Binary Search Tree (BST).
  Step 2 — Brute force: Check at each node if left<node<right.
  Step 3 — Why brute force is incomplete: Doesn't validate subtree constraints!
           Left subtree ALL < node, right subtree ALL > node.
  Step 4 — Optimised approach: Maintain valid range [min, max] for each node.
  Step 5 — Edge cases: Null nodes? Single node?

Approach: Recursive validation with range constraints
Time complexity:  O(n) — visit each node
Space complexity: O(h) — h = height
"""

class TreeNode:
    """Node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    Check if binary tree is a valid Binary Search Tree.
    BST: left < node < right (for ALL ancestors too).
    """
    def validate(node, min_val, max_val):
        """
        Recursively validate with range constraints.
        min_val: All values in this subtree must be > min_val.
        max_val: All values in this subtree must be < max_val.
        """
        # Base case: empty tree is valid
        if not node:
            return True
        
        # Check if current node violates constraints
        # Why: Must be within valid range
        if node.val <= min_val or node.val >= max_val:
            return False
        
        # Validate left subtree
        # Why: All left values must be < node.val
        if not validate(node.left, min_val, node.val):
            return False
        
        # Validate right subtree
        # Why: All right values must be > node.val
        if not validate(node.right, node.val, max_val):
            return False
        
        return True
    
    # Start with infinite range
    return validate(root, float('-inf'), float('inf'))

# ── Test cases ────────────────────────────

print("Test 1 (Valid BST):")
#       2
#      / \
#     1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(f"Is valid BST: {isValidBST(root)}")  # Expected: True

print("\nTest 2 (Invalid BST):")
#       5
#      / \
#     1   4
#        / \
#       3   6
# Invalid: 4 is in right subtree of 5, but 3 < 5
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(f"Is valid BST: {isValidBST(root)}")  # Expected: False

print("\nTest 3 (Single node):")
root = TreeNode(0)
print(f"Is valid BST: {isValidBST(root)}")  # Expected: True

print("\nTest 4 (Edge case):")
#       1
#        \
#         1
root = TreeNode(1)
root.right = TreeNode(1)
print(f"Is valid BST: {isValidBST(root)}")  # Expected: False (equal not allowed)
