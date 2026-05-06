class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zero_count = 0
        mult_nonzero = 1
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            else:
                mult_nonzero *= nums[j]
            mult *= nums[j]

        rlist = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_count <= 1:
                    rlist.append(mult_nonzero)
                else:
                    rlist.append(0)
            else:
                rlist.append(mult // nums[i])

        return rlist