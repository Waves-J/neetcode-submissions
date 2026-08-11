class Solution:
    def rob(self, nums: List[int]) -> int:
        first = self.rob1(nums[:len(nums) - 1])
        second = self.rob1(nums[1:])
        return max(first, second) if len(nums) > 1 else nums[0]


    def rob1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

        # n = len(nums)
        # dp = [-1] * len(nums)

        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
        #     return dp[i]
        
        # return max(dfs(0), dfs(1))  