class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # Now 'i' is the last instance of this duplicate. 
            backtrack(i + 1)

        backtrack(0)
        return result