class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, amt):            
            if i == len(nums):
                if amt == target:
                    return 1
                else:
                    return 0
            
            if (i, amt) in dp:
                return dp[(i, amt)]
            
            dp[(i, amt)] = dfs(i + 1, amt + nums[i]) + dfs(i + 1, amt - nums[i])

            return dp[(i, amt)] 

        return dfs(0, 0)
