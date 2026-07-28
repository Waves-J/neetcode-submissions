class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        linked = {}
        self.isCycle = False
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
                    self.isCycle = True
                elif edge not in black and edge != p:
                    dfs(edge, v)
            
            gray.remove(v)
            black.add(v)

        dfs(0, None)
        
        return not self.isCycle and (len(black) == n)