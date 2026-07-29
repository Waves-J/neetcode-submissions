class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def dfs(n, p):
            if n in visited:
                return
            
            visited.add(n)
            for neighbour in adj[n]:
                if neighbour == p:
                    continue
                dfs(neighbour, n)
                   
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        
        return count