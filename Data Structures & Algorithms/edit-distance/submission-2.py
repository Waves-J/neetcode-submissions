class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if len(word1) == 0:
                return len(word2)
            if len(word2) == 0:
                return len(word1)
            
            if j == len(word2):
                return len(word1) - i
            
            if i == len(word1):
                return len(word2) - j
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            dp[(i, j)] = min(dfs(i + 1, j + 1) + 1, dfs(i + 1, j) + 1, dfs(i, j + 1) + 1)

            return dp[(i, j)]

        return dfs(0, 0)