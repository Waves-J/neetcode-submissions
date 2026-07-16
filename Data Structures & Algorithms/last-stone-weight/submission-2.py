import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            second = stones[1] if len(stones) == 2 else max(stones[1], stones[2])
            new_stone = stones[0] - second
            heapq.heappop_max(stones)
            heapq.heappop_max(stones)
            if new_stone > 0:
                heapq.heappush_max(stones, new_stone)

        return stones[0] if stones else 0