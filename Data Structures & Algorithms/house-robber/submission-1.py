class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * len(nums)

        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return dp[i]
        
        return max(dfs(0), dfs(1))  