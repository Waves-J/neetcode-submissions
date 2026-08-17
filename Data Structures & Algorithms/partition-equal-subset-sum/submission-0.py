class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(n - 1, -1, -1):
            next_dp = set()
            for j in dp:
                next_dp.add(nums[i] + j)
                next_dp.add(j)
            dp = next_dp
        
        return True if target in dp else False
                