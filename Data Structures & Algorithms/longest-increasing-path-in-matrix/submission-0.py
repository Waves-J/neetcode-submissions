class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                down, up, right, left = 1, 1, 1, 1
                visit.add((i, j))
                if i + 1 < len(matrix) and (i + 1, j) not in visit and matrix[i][j] < matrix[i + 1][j]:
                    down = dfs(i + 1, j) + 1
                
                if i - 1 >= 0 and (i - 1, j) not in visit and matrix[i][j] < matrix[i - 1][j]:
                    up = dfs(i - 1, j) + 1
                
                if (j + 1 < len(matrix[0]) and
                    (i, j + 1) not in visit and 
                    matrix[i][j] < matrix[i][j + 1]):
                    right = dfs(i, j + 1) + 1
                
                if j - 1 >= 0 and (i, j - 1) not in visit and matrix[i][j] < matrix[i][j - 1]:
                    left = dfs(i, j - 1) + 1
                
                visit.remove((i, j))
                dp[(i, j)] = max(down, up, right, left)
                return dp[(i, j)]

            return 0

        most = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visit = set()
                curr = dfs(i, j)
                if curr > most:
                    most = curr
        
        return most