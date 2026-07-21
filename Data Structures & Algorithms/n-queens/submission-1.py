from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        part = []
        used = defaultdict(int)

        def backtrack(i):
            if i == n:
                result.append(part[:])
                return
            
            for j in range(n):
                if (i, j) not in used or used[(i, j)] == 0:
                    part.append("."*j + "Q" + "."*(n - j - 1))

                    for k in range(n):
                        used[(k, j)] += 1
                    l = 0
                    while i + l < n and j + l < n:
                        used[(i + l, j + l)] += 1
                        l += 1
                    l = 1
                    while i + l < n and j - l >= 0:
                        used[(i + l, j - l)] += 1
                        l += 1

                    backtrack(i + 1)
                    part.pop()
                    
                    for k in range(n):
                        used[(k, j)] -= 1
                    l = 0
                    while i + l < n and j + l < n:
                        used[(i + l, j + l)] -= 1
                        l += 1
                    l = 1
                    while i + l < n and j - l >= 0:
                        used[(i + l, j - l)] -= 1
                        l += 1
                    
                    
        backtrack(0)
        return result