class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        max_heap = []
        max_list = []

        for i in range(k):
            heapq.heappush_max(max_heap, (nums[i], i))
        
        left = 0

        while left + k <= len(nums):
            max_list.append(max_heap[0][0])
            if max_heap[0][0] == nums[left]:
                heapq.heappop_max(max_heap)
                while len(max_heap) > 1 and max_heap[0][1] < left:
                    heapq.heappop_max(max_heap)
            if left + k < len(nums):
                heapq.heappush_max(max_heap, (nums[left + k], left + k))
            left += 1
        
        return max_list
