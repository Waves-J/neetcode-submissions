# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True
        
        def dfs_depth(node):
            if not node:
                return 0
            
            left_depth = dfs_depth(node.left)
            right_depth = dfs_depth(node.right)

            if abs(left_depth - right_depth) > 1:
                self.balanced = False

            return 1 + max(left_depth, right_depth)

        dfs_depth(root)
        return self.balanced
