class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        sell_pointer = 0

        max_profit = 0
        for i, price in enumerate(prices):
            if prices[sell_pointer] <= price:
                sell_pointer = i
            else:
                max_profit += prices[sell_pointer] - prices[buy_pointer]
                buy_pointer = i
                sell_pointer = i
        
        if buy_pointer != sell_pointer:
            max_profit += prices[sell_pointer] - prices[buy_pointer]
        return max_profit