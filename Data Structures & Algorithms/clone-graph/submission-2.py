"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        def dfs(v):
            new = Node(v.val)
            old_to_new[v] = new

            for u in v.neighbors:
                if u not in old_to_new:
                    dfs(u)
                new.neighbors.append(old_to_new[u])
                
            return new

        return dfs(node)


