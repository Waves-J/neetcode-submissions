class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curr_min, curr_max = 1, 1

        for num in nums:
            temp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(temp, curr_min * num, num)
            result = max(result, curr_max)
        
        return result
            

            



