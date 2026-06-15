class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_bound = []
        right_bound = []
        for i in range(len(heights)):
            j = i
            while j + 1 < len(heights) and heights[i] <= heights[j + 1]:
                j += 1
            right_bound.append(j)
        
        for i in range(len(heights)):
            j = i
            while j - 1 >= 0 and heights[i] <= heights[j - 1]:
                j -= 1
            left_bound.append(j)
        
        largest_area = 0

        for i in range(len(heights)):
            area = heights[i] * (right_bound[i] - left_bound[i] + 1)
            if area > largest_area:
                largest_area = area
        
        return largest_area

            