class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(times)):
            adj[times[i][0]].append((times[i][1], times[i][2]))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            
            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)
            
        dfs(k, 0)
        result = max(dist.values())
        return result if result < float('inf') else -1