# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levelOrder = []

        def bfs(node, depth):
            if not node:
                return 0

            if len(self.levelOrder) <= depth:
                self.levelOrder.append([])
            
            self.levelOrder[depth].append(node.val)
            
            left = bfs(node.left, depth + 1)
            right = bfs(node.right, depth + 1)
        
        bfs(root, 0)
        return self.levelOrder