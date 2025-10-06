class Solution(object):
    def maxProfit(self, prices):
        min_buy_rate = float('inf')
        max_profit = 0
        
        for price in prices:
            min_buy_rate = min(min_buy_rate, price)
            max_profit = max(max_profit, price - min_buy_rate)

        return max_profit
'''
[7, 1, 5, 3, 6, 4]
             |
min_buy = 1
max_profit = 5
'''