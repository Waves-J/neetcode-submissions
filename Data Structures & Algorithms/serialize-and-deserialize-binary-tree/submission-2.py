# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.strings = []

        def dfs(node):
            if not node:
                self.strings.append("N")
                return
            
            self.strings.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        return ",".join(self.strings)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.nodes = data.split(",")
        self.i = 0

        def dfs():
            if self.nodes[self.i] == "N":
                self.i += 1
                return None
        
            node = TreeNode(int(self.nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

