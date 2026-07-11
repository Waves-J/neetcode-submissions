# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        def dfs_depth(node):
            if not node:
                return 0
            
            left_depth = dfs_depth(node.left)
            right_depth = dfs_depth(node.right)

            return 1 + max(left_depth, right_depth)

        left_height = dfs_depth(root.left)
        right_height = dfs_depth(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
