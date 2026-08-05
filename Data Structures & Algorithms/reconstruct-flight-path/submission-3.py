class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        result = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            result.append(src)

        dfs("JFK")
        return result[::-1]
    