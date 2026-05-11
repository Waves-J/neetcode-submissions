class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxarea = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > maxarea:
                maxarea = area
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxarea
