class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        word_len = len(word)

        def backtrack(row: int, col: int, idx: int) -> bool:
            if idx == word_len:
                return True
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_row, n_col = row + x, col + y
                if not (0 <= n_row < n and 0 <= n_col < m) or board[n_row][n_col] == '#':
                    continue
                
                if board[n_row][n_col] == word[idx]:
                    temp = board[n_row][n_col]
                    board[n_row][n_col] = '#'
                    if backtrack(n_row, n_col, idx + 1):
                        return True
                    board[n_row][n_col] = temp
                
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    hold = board[i][j]
                    board[i][j] = '#'
                    if word_len == 1:
                        return True
                    elif backtrack(i, j, 1):
                        return True
                    board[i][j] = hold
        return False