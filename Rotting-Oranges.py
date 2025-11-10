class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs approach
        # first iteration, find all the rotten oranges first and add them to explore
        # while you do that remember the number of total oranges, and the rotten oranges

        # pop from explore, add to visit, add new neighbors to explore
        # after the explore is empty, check if the num of rotten oranges = total oranges
        m = len(grid)
        n = len(grid[0])

        from collections import deque
        explore = deque()

        num_rotten = 0
        num_total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 2:
                    explore.append((i, j))
                    num_rotten += 1
                num_total += 1

        minute_counter = 0
        while explore:
            for _ in range(len(explore)):  # current level
                i, j = explore.popleft()

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        num_rotten += 1
                        explore.append((x, y))

            if explore:
                minute_counter += 1

        return minute_counter if num_rotten == num_total else -1
        # dp approach
        # sub-problem: how many
        # base-case:
        # recurrence: