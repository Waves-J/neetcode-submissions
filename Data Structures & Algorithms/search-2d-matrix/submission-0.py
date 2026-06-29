class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        row = -1

        while i <= j:
            m = (j + i) // 2
            if matrix[m][0] > target:
                j = m - 1
            elif matrix[m][0] < target:
                row = m
                i = m + 1
            else:
                return True
        
        if row == -1:
            return False

        if row >= len(matrix):
            row -= 1
        
        i = 0
        j = len(matrix[row]) - 1

        while i <= j:
            m = (j + i) // 2
            if matrix[row][m] > target:
                j = m - 1
            elif matrix[row][m] < target:
                i = m + 1
            else:
                return True

        return False
            


