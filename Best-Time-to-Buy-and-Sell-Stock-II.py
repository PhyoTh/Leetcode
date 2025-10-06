class Solution(object):
    def maxProfit(self, prices):
        index = 0
        total_profit = 0
        local_max = prices[0]
        local_min = prices[0]

        while index < len(prices) - 1:
            while (index < len(prices)-1) and (prices[index] >= prices[index+1]):
                index += 1
            local_min = prices[index]
            while (index < len(prices)-1) and (prices[index] <= prices[index+1]):
                index += 1
            local_max = prices[index]
            total_profit += local_max - local_min
        return total_profit