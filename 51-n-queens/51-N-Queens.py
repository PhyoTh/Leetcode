class Solution:
    def populateBoard(self, queens: list) -> list:
        n = len(queens)
        board = []
        for col in queens:
            temp = ('.' * col) + 'Q' + ('.' * (n - col - 1))
            board.append(temp)
        return board

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def backtrack(row: int, seen_cols: set, invalid_d1: set, invalid_d2: set, queens: list):
            if len(queens) == n:
                board = self.populateBoard(queens)
                result.append(board)
                return
            
            for col in range(n):
                if col not in seen_cols and row - col not in invalid_d1 and row + col not in invalid_d2:
                    seen_cols.add(col)
                    invalid_d1.add(row - col)
                    invalid_d2.add(row + col)
                    queens.append(col)
                    
                    backtrack(row + 1, seen_cols, invalid_d1, invalid_d2, queens)
                    invalid_d1.remove(row - col)
                    invalid_d2.remove(row + col)
                    seen_cols.remove(col)
                    queens.pop()
        
        backtrack(0, set(), set(), set(), [])
        return result