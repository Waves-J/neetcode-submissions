class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def dfs(i):
            if i == len(s):
                result.append(part[:])
                return

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return result

    def isPalin(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True