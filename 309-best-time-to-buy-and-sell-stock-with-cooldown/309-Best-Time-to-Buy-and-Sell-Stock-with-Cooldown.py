class Solution:
    '''
    i = 0, 1, 2, 3, 4
       [1, 2, 3, 0, 2]

    basecases:
        dp[0][0] = - prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

    at i == 2:
        case 0: you have long_hold, you bought it today, or keep holding previous
            dp[i][0] = max(dp[i - 1][2] - prices[i], dp[i - 1][0])
        case 1: you don't have long_hold, you sold it today
            dp[i][1] = dp[i - 1][0] + prices[i]
        case 2: you are on resting state, didn't sell yesterday or did sell yesterday
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
    
    return:
        max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
    '''
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        hold = [0 for _ in range(n)]
        sold = [0 for _ in range(n)]
        rest = [0 for _ in range(n)]

        hold[0] = - prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i]) # keep holding previous, or buy on resting
            sold[i] = hold[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sold[i - 1])
        return max(hold[n - 1], sold[n - 1], rest[n - 1])