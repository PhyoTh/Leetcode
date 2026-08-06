from collections import deque
EMPTY = 2147483647
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms), len(rooms[0])
        que = deque()

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    que.append((i, j))
        
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()

                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    n_row, n_col = row + x, col + y
                    if not (0 <= n_row < n and 0 <= n_col < m) or rooms[n_row][n_col] == -1 or rooms[n_row][n_col] == 0 or rooms[n_row][n_col] != EMPTY:
                        continue
                    
                    rooms[n_row][n_col] = min(rooms[n_row][n_col], rooms[row][col] + 1)
                    que.append((n_row, n_col))
        
        return rooms
