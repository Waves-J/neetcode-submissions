import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        
        for point in points:
            x, y = point[0], point[1]
            heap.append(((((x)**2 + (y)**2))**0.5, point))

        heapq.heapify(heap)

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
