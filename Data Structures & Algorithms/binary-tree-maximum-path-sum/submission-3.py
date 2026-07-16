# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxpath = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            if node.val + left_max + right_max > self.maxpath:
                self.maxpath = node.val + left_max + right_max

            return node.val + max(left_max, right_max)
                
        dfs(root)
        return self.maxpath