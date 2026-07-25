class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        self.max_area = 0

        def dfs(row, col):
            if (min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0 or (row, col) in visited):
                return 0
            
            visited.add((row, col))
            
            return 1 + dfs(row - 1, col) +  dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col)
                    if area > self.max_area:
                        self.max_area = area
        
        return self.max_area       