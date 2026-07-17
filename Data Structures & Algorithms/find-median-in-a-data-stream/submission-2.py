import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= self.maxheap[0]:
            heapq.heappush_max(self.maxheap, num)
        else:
            heapq.heappush(self.minheap, num)

        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, heapq.heappop_max(self.maxheap))
        elif len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        else:
            return (self.maxheap[0] + self.minheap[0]) / 2
        