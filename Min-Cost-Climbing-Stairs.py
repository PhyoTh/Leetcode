class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # subproblem:
        # dp_minCost[i] : minimum number of steps to get to ith step
        dp_minCost = [float('inf')] * (len(cost) + 1)

        # base cases
        dp_minCost[0] = cost[0]
        dp_minCost[1] = cost[1]

        for i in range(2, len(dp_minCost)):
            current_cost = cost[i] if i < len(cost) else 0
            dp_minCost[i] = min(dp_minCost[i - 1], dp_minCost[i - 2]) + current_cost

        return dp_minCost[len(cost)]
