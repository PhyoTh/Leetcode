class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost) + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost) + 1):
            cur = cost[i] if i < len(cost) else 0
            dp[i] = min(dp[i - 2], dp[i - 1]) + cur
        return dp[len(cost)]
