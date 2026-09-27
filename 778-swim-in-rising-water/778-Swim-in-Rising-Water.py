import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        while heap:
            elv, row, col = heapq.heappop(heap)
            if (row, col) == (n - 1, n - 1):
                return elv

            for x, y in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                n_row, n_col = row + x, col + y
                if not (0 <= n_row < n and 0 <= n_col < n) or (n_row, n_col) in visited:
                    continue
                
                n_elv = max(elv, grid[n_row][n_col])
                heapq.heappush(heap, (n_elv, n_row, n_col))
                visited.add((n_row, n_col))
        return cost[(n - 1, n - 1)]