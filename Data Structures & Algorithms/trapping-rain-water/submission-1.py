class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0] * len(height)
        max_num = 0
        for i in range(len(height)):
            leftmax[i] = max_num
            if max_num < height[i]:
                max_num = height[i]

        rightmax = [0] * len(height)
        max_num = 0
        for i in range(len(height) - 1, -1, -1):
            rightmax[i] = max_num
            if max_num < height[i]:
                max_num = height[i]

        watersum = 0
        for i in range(len(height)):
            if min(leftmax[i], rightmax[i]) - height[i] > 0:
                watersum += min(leftmax[i], rightmax[i]) - height[i]
        
        return watersum
             
            