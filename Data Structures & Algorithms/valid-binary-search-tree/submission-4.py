# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValidBST = True

        def dfs(node, largest, smallest):
            if not node:
                return 0

            if node.val <= smallest or node.val >= largest:
                self.isValidBST = False
            
            dfs(node.left, min(node.val, largest), smallest)
            dfs(node.right, largest, max(node.val, smallest))

        dfs(root, float('inf'), float('-inf'))

        return self.isValidBST