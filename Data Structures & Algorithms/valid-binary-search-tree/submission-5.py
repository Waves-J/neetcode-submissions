# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, largest, smallest):
            if not node:
                return True

            if node.val <= smallest or node.val >= largest:
                return False
            
            return dfs(node.left, node.val, smallest) and dfs(node.right, largest, node.val)

        return dfs(root, float('inf'), float('-inf'))