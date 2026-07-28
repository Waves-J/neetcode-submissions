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
            if v in black:
                return

            gray.add(v)
            for edge in linked[v]:
                if edge in gray and edge != p:
                    return False
                elif edge not in black and edge != p:
                    if not dfs(edge, v):
                        return False
            
            gray.remove(v)
            black.add(v)
            return True


        return dfs(0, None) and (len(black) == n)