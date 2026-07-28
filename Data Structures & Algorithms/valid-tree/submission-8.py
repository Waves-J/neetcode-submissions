class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(n, p):
            if n in visited:
                return False
            
            visited.add(n)
            for neighbour in adj[n]:
                if neighbour == p:
                    continue
                if not dfs(neighbour, n):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n