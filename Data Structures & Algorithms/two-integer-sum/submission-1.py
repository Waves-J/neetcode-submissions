class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()
        for i in range(len(nums)):
            hashset.add(target - nums[i])
        for i in range(len(nums)):
            if nums[i] in hashset:
                for j in range(len(nums)):
                    if j != i and nums[j] == target - nums[i]:
                        return [i, j]