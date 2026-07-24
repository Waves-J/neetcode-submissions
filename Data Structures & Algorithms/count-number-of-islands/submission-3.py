class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        visited = set()

        def dfs(row, col):
            if (min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0" or (row, col) in visited):
                return
            
            visited.add((row, col))
            
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    self.count += 1
        
        return self.count