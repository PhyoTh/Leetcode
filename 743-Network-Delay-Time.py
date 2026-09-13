from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n + 1)]
        for frm, to, time in times:
            adj_list[frm].append((to, time))
        
        que = deque([(k, 0)])
        costs = {k: 0}
        while que:
            node, cost = que.popleft()
            
            for neighbor, time in adj_list[node]:
                new_price = cost + time

                if neighbor not in costs or costs[neighbor] > new_price:
                    costs[neighbor] = new_price
                    que.append((neighbor, new_price))

        return max(costs.values()) if len(costs) == n else -1

'''
adj_list =
[
[],
[(2, 1)],
[(1, 3)]
]


'''