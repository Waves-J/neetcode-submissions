# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxpath = float("-inf")
        
        def dfs(node, one_path):
            if not node:
                return 0
            
            left_one_path = max(0, dfs(node.left, True))
            right_one_path = max(0, dfs(node.right, True))

            dfs(node.left, False)
            dfs(node.right, False)

            if not one_path:
                if node.val + left_one_path + right_one_path > self.maxpath:
                    self.maxpath = node.val + left_one_path + right_one_path
                return node.val + left_one_path + right_one_path

            else:
                if left_one_path > right_one_path:
                    if node.val + left_one_path > self.maxpath:
                        self.maxpath = node.val + left_one_path
                    return node.val + left_one_path
                else:
                    if node.val + right_one_path > self.maxpath:
                        self.maxpath = node.val + right_one_path
                    return node.val + right_one_path
                
        
        dfs(root, False)
        return self.maxpath