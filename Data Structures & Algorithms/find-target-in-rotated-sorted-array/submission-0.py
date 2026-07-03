class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1
        
        min_index = m
        minimum = nums[m]

        i = min_index
        j = min_index + len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m % len(nums)] < target:
                i = m + 1
            elif nums[m % len(nums)] > target:
                j = m - 1
            else:
                return m % len(nums)

        return -1
