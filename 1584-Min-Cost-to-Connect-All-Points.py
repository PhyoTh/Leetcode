class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = [float('inf') for _ in range(len(points))]
        costs[0] = 0
        tree = set()
        
        while len(tree) < len(points): # O(n)
            min_node = None
            for i in range(len(points)): # O(n)
                if i in tree:
                    continue
                if min_node == None:
                    min_node = i
                    continue
                min_node = i if costs[i] < costs[min_node] else min_node
            
            tree.add(min_node)
            for i in range(len(points)): # O(n)
                if i in tree:
                    continue
                
                new_cost = abs(points[i][0] - points[min_node][0]) + abs(points[i][1] - points[min_node][1])
                if new_cost < costs[i]:
                    costs[i] = new_cost

        return sum(costs) if len(tree) == len(points) else -1