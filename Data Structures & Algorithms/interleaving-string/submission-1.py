class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(i1, i2):
            first, second = False, False
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            if i1 + i2 == len(s3):
                return True

            if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                first = dfs(i1 + 1, i2)
            
            if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                second = dfs(i1, i2 + 1)
            
            dp[(i1, i2)] = first or second

            return dp[(i1, i2)]

        if len(s1) + len(s2) != len(s3):
            return False

        return dfs(0, 0)



        



        