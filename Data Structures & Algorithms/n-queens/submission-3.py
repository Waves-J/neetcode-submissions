from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        part = []
        col = set()
        diagPos = set()
        diagNeg = set()

        def backtrack(i):
            if i == n:
                result.append(part[:])
                return
            
            for j in range(n):
                if j not in col and i + j not in diagPos and i - j not in diagNeg:
                    part.append("."*j + "Q" + "."*(n - j - 1))

                    col.add(j)
                    diagPos.add(i + j)
                    diagNeg.add(i - j)

                    backtrack(i + 1)
                    part.pop()

                    col.remove(j)
                    diagPos.remove(i + j)
                    diagNeg.remove(i - j)

        backtrack(0)
        return result