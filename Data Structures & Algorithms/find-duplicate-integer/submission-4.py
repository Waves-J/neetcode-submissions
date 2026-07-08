class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection point in the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]           # 1 step
            fast = nums[nums[fast]]     # 2 steps
            if slow == fast:
                break
        
        # Phase 2: Find the "entrance" to the cycle (the duplicate)
        slow2 = 0
        while True:
            slow = nums[slow]           # 1 step
            slow2 = nums[slow2]         # 1 step
            if slow == slow2:
                return slow


        """
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1
            if nums[abs(nums[i]) - 1] > 0:
                return abs(nums[i])
        """
