class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        res = 0

        def dfs(i, a):
            if a > amount or i == len(coins):
                return 0
            
            if a == amount:
                return 1
            
            if (i, a) in dp:
                return dp[(i, a)]
            
            stay = dfs(i, a + coins[i])
            proceed = dfs(i + 1, a)

            dp[(i, a)] = stay + proceed

            return dp[(i, a)]
        
        return dfs(0, 0)