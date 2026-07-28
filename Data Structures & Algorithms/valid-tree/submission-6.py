class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        linked = {}
        gray = set()
        black = set()
        
        for i in range(n):
            linked[i] = []
        for edge in edges:
            linked[edge[1]].append(edge[0])
            linked[edge[0]].append(edge[1])

        def dfs(v, p):
            gray.add(v)
            for adj in linked[v]:
                if adj != p:
                    if adj in gray:
                        return False
                    elif adj not in black:
                        if not dfs(adj, v):
                            return False
            
            gray.remove(v)
            black.add(v)
            return True

        return dfs(0, None) and (len(black) == n)