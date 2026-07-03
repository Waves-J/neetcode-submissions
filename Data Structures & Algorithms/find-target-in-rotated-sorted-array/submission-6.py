class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] < nums[j]:
                if target >= nums[m] and target <= nums[j]:
                    k = m
                    l = j

                    while k <= l:
                        mid = (k + l) // 2
                        if nums[mid] > target:
                            l = mid - 1
                        elif nums[mid] < target:
                            k = mid + 1
                        else:
                            return mid

                j = m
            else:
                if target <= nums[m] and target >= nums[i]:
                    k = i
                    l = m

                    while k <= l:
                        mid = (k + l) // 2
                        if nums[mid] > target:
                            l = mid - 1
                        elif nums[mid] < target:
                            k = mid + 1
                        else:
                            return mid

                i = m + 1
        
        return -1
        