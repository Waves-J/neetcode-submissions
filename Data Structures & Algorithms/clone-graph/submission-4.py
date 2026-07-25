"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        
        def dfs(v):
            if v in old_to_new:
                return old_to_new[v]

            new = Node(v.val)
            old_to_new[v] = new

            for u in v.neighbors:
                new.neighbors.append(dfs(u))
                
            return new

        return dfs(node) if node else None


