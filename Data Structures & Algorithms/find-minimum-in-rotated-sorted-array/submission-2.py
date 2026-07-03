class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1
        
        return nums[m]

