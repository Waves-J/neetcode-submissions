class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(sub, curr):
            if curr < len(nums):
                backtrack(sub, curr + 1)
                backtrack(sub + [nums[curr]], curr + 1)
            else:
                self.result.append(sub)
            
        backtrack([], 0)

        return self.result