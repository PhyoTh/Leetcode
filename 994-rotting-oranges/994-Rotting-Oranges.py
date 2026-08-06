from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        minute = 0

        que = deque()
        total_oranges = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                
                total_oranges += 1
                if grid[i][j] == 2:
                    que.append((i, j))
                
        rotten_oranges = 0
        while que:
            minute += 1 if rotten_oranges != 0 else 0
            rotten_oranges += len(que)
            for _ in range(len(que)):
                row, col = que.popleft()

                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    n_row, n_col = row + x, col + y
                    if not (0 <= n_row < n and 0 <= n_col < m) or grid[n_row][n_col] == 2 or grid[n_row][n_col] == 0:
                        continue
                    
                    grid[n_row][n_col] = 2
                    que.append((n_row, n_col))

        return minute if rotten_oranges == total_oranges else -1