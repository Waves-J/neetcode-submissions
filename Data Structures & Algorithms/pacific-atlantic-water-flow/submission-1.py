class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, isRoot):
            if (r, c) in visited:
                return
            if r == 0 or c == 0:
                self.pacific = True
            if r == len(heights) - 1 or c == len(heights[0]) - 1:
                self.atlantic = True

            
            visited.add((r, c))
            for rd, cd in directions:
                row, col = r + rd, c + cd
                if (0 <= row < len(heights)
                    and 0 <= col < len(heights[0])
                    and heights[r][c] >= heights[row][col]
                    ):
                    dfs(row, col, False)
            
            if self.pacific and self.atlantic and isRoot:
                result.append([r, c])

            return
            
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                visited = set()
                self.pacific = False
                self.atlantic = False
                dfs(r, c, True)
        
        return result