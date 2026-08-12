class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        result_index = 0
        result_length = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1) > result_length:
                        result_length = j - i + 1
                        result_index = i
        
        return s[result_index:result_index + result_length]