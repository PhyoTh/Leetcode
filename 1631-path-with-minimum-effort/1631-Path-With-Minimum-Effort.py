import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])

        heap = [(0, 0, 0)] # (max_cost, row, col)
        costs = {(0, 0): 0}

        while heap:
            cur_cost, row, col = heapq.heappop(heap)
            if cur_cost > costs[(row, col)]:
                continue
            
            if (row, col) == (n - 1, m - 1):
                return cur_cost

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_row, n_col = row + x, col + y
                if not (0 <= n_row < n and 0 <= n_col < m):
                    continue
                
                n_cost = max(cur_cost, abs(heights[row][col] - heights[n_row][n_col]))
                if (n_row, n_col) in costs and costs[(n_row, n_col)] <= n_cost:
                    continue
                heapq.heappush(heap, (n_cost, n_row, n_col))
                costs[(n_row, n_col)] = n_cost
        return -1