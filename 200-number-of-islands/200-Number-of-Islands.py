class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        grid[row][col] = '0'

                        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            n_row, n_col = row + x, col + y
                            if not (0 <= n_row < n and 0 <= n_col < m):
                                continue
                            
                            if grid[n_row][n_col] == '1':
                                stack.append((n_row, n_col))
                    islands += 1

        return islands