
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 0
                    area = 0
                    while stack:
                        row, col = stack.pop()
                        area += 1

                        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            n_row, n_col = row + x, col + y
                            if not (0 <= n_row < n and 0 <= n_col < m):
                                continue
                            
                            if grid[n_row][n_col] == 1:
                                grid[n_row][n_col] = 0
                                stack.append((n_row, n_col))
                    max_area = max(max_area, area)
    
        return max_area