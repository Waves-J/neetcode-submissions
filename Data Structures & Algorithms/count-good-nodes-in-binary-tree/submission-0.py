# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodCount = 0

        def dfs(node, max_from_path):
            if not node:
                return 0

            if node.val >= max_from_path:
                self.goodCount += 1
                max_from_path = node.val
            
            dfs(node.left, max_from_path)
            dfs(node.right, max_from_path)

        dfs(root, float('-inf'))

        return self.goodCount



