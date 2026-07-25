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
            if v in old_to_new:
                return

            if v not in old_to_new:
                new = Node(v.val)
                old_to_new[v] = new
            else:
                new = old_to_new[v]

            for u in v.neighbors:
                if u not in old_to_new:
                    dfs(u)
                new.neighbors.append(old_to_new[u])
                
            return new

        return dfs(node)


