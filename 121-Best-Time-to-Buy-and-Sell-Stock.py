class Solution(object):
    def maxProfit(self, prices):
        minPrice = sys.maxsize
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit

        