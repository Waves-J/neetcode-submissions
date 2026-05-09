class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rlist = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in rlist:
                        rlist.append([nums[i], nums[j], nums[k]])
                    j += 1

        return rlist
