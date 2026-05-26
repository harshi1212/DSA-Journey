"""
TEMPLATE: Binary Tree Traversals
Use for: Tree problems, DFS, backtracking
Complexity: O(n) - visit each node once
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    """Left - Root - Right"""
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

def preorder(root):
    """Root - Left - Right"""
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return result

def postorder(root):
    """Left - Right - Root"""
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    dfs(root)
    return result

def level_order(root):
    """BFS level traversal"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Usage:
print("Template 6: Binary Tree Traversals")

# Build tree:    1
#               / \
#              2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(f"Inorder: {inorder(root)}")
print(f"Preorder: {preorder(root)}")
print(f"Postorder: {postorder(root)}")
print(f"Level order: {level_order(root)}")
