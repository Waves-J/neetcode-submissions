class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                area = h * w
                if area > largest_area:
                    largest_area = area
            
            stack.append(i)
        
        
        return largest_area

            