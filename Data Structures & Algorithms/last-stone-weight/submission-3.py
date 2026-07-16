import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            largest, second = heapq.heappop_max(stones), heapq.heappop_max(stones)
            new_stone = largest - second
            if new_stone > 0:
                heapq.heappush_max(stones, new_stone)

        return stones[0] if stones else 0