class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        subproblem:
            min_cost[i] -> minimum cost up to day i-th
        base case:
            min_cost[0] = 0
            min_cost[1] = costs[0]
        recurrence relation:
            for day i, you can buy with
            1. i - 1 th day with cost of 1 day pass
            2. i - 7 th day with cost of 7 day pass
            3. i - 30 th day with cost of 30 day pass
        '''
        days_set = set(days)
        max_day_to_cover = days[-1]

        # from 0 to max_day each min_cost[i] represent the min cost up to day i
        min_cost = [0] * (max_day_to_cover + 1)

        for day in range(1, max_day_to_cover + 1):
            if day not in days_set:
                min_cost[day] = min_cost[day - 1]
                continue

            one_day_pass = min_cost[day - 1] + costs[0]
            seven_day_pass = min_cost[max(0, day - 7)] + costs[1]
            thirty_day_pass = min_cost[max(0, day - 30)] + costs[2]

            min_cost[day] = min(one_day_pass, seven_day_pass, thirty_day_pass)

        return min_cost[max_day_to_cover]
