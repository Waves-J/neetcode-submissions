import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        heap = []
        time = 0
        queue = deque()
        
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 1
            else:
                hashmap[task] += 1
        
        for key, value in hashmap.items():
            heapq.heappush_max(heap, [value, key])
        
        while queue or heap:
            if queue:
                if queue[0][0] <= time:
                    heapq.heappush_max(heap, queue.popleft()[1])
            if heap:
                task = heapq.heappop_max(heap)
                task[0] -= 1
                if task[0] > 0:
                    queue.append([time + n + 1, task])
                time += 1
            else:
                time = queue[0][0]
        
        return time
        

