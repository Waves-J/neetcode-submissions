class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, idx):
            if idx == len(nums):
                self.res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        self.res = []
        backtrack(nums, 0)
        return self.res