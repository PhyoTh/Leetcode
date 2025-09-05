class Solution(object):
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        islands = 0

        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1":
                    islands += 1
                    grid[x][y] = "0" # mark as visited
                    # self.bfs(grid, x, y)
                    self.dfs(grid, x, y)
        
        return islands

    def bfs(self, grid, row, col):
        from collections import deque
        explore = deque([(row, col)])

        while len(explore) != 0:
            current = explore.popleft()
            for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]: # top, down, left, right
                Xrow = current[0] + x
                Ycol = current[1] + y
                if 0 <= Xrow < len(grid) and 0 <= Ycol < len(grid[0]): # if its in the grid
                    if grid[Xrow][Ycol] == "1":
                        explore.append((Xrow, Ycol))
                        grid[Xrow][Ycol] = "0" # mark as visited

    def dfs(self, grid, row, col):
        from collections import deque
        explore = deque([(row, col)])
    
        while len(explore) != 0:
            current = explore.pop()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                Xrow = current[0] + x
                Ycol = current[1] + y
                if 0 <= Xrow < len(grid) and 0 <= Ycol < len(grid[0]): # if its in the grid
                    if grid[Xrow][Ycol] == "1":
                        grid[Xrow][Ycol] = "0"
                        self.dfs(grid, Xrow, Ycol)