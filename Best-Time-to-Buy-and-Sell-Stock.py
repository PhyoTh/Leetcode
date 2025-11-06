class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0
        
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        
        return max_profit