from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for frm, to, price in flights:
            adj_list[frm].append((to, price))
        
        que = deque([(src, 0)])
        costs = {src: 0}
        stop = -1

        while que and stop < k:
            stop += 1
            for _ in range(len(que)):
                node, cost = que.popleft()

                for neighbor, price in adj_list[node]:
                    new_price = cost + price

                    if neighbor not in costs or costs[neighbor] > new_price:
                        costs[neighbor] = new_price
                        que.append((neighbor, new_price))
        
        return costs.get(dst, -1)