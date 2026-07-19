class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        self.curr = 0

        def backtrack(starting_index):
            if self.curr < target:
                for k in range(starting_index, len(nums)):
                    self.curr += nums[k]
                    subset.append(nums[k])
                    backtrack(k)
                    self.curr -= subset.pop()

            elif self.curr == target:
                result.append(subset[:])

        backtrack(0)
        return result      