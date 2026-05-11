class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 100

        for i in range(len(prices)):
            if prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy
            if prices[i] < min_buy:
                min_buy = prices[i]
        
        return max_profit



