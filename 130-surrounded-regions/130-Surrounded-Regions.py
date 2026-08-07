from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        que = deque()

        row, col = 0, 0
        started = False
        while (row, col) != (0, 0) or not started:
            started = True
            if board[row][col] == 'O':
                que.append((row, col))
                board[row][col] = '#'
            
            if row == 0 and col < m - 1:
                col += 1
            elif col == m - 1 and row < n - 1:
                row += 1
            elif row == n - 1 and col > 0:
                col -= 1
            elif col == 0 and row > 0:
                row -= 1
        
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()

                for x, y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                    n_row, n_col = row + x, col + y
                    if not (0 <= n_row < n and 0 <= n_col < m) or board[n_row][n_col] == 'X' or board[n_row][n_col] == '#':
                        continue
                    
                    board[n_row][n_col] = '#'
                    que.append((n_row, n_col))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'