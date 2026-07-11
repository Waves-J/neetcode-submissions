# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.isSame = True
        
        def dfs_depth(node1, node2):
            if not node1 and not node2:
                return 0, 0

            if (not node1 and node2) or (node1 and not node2):
                self.isSame = False
                return 0, 0
            
            left1, left2 = dfs_depth(node1.left, node2.left)
            right1, right2 = dfs_depth(node1.right, node2.right)

            if node1.val != node2.val:
                self.isSame = False

            return 1 + max(left1, right1), 1 + max(left2, right2)

        dfs_depth(p, q)
        return self.isSame
            
