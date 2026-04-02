1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n == 1:
4            return 1
5        
6        dp = [0 for _ in range(n)]
7        dp[0] = 1 # 1 step
8        dp[1] = 2 # 2 step
9        for i in range(2, n):
10            dp[i] = dp[i - 1] + dp[i - 2] # 1 step or 2 step
11        return dp[n - 1]