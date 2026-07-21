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
        return s[left:right + 1] == s[left:right + 1][::-1]