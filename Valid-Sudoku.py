class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # one row needs only 1 check
        def checkRow(row) -> bool:
            seen = set()
            for i in range(n):
                if board[row][i].isdigit():
                    if board[row][i] in seen:
                        return False
                    seen.add(board[row][i])
            return True

        # one col needs only 1 check
        def checkCol(col) -> bool:
            seen = set()
            for i in range(n):
                if board[i][col].isdigit():
                    if board[i][col] in seen:
                        return False
                    seen.add(board[i][col])
            return True

        # one 3x3 needs only 1 check
        def check3by3(row, col) -> bool:
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j].isdigit():
                        if board[row+i][col+j] in seen:
                            return False
                        seen.add(board[row+i][col+j])
            return True

        # main starts here
        # check each row
        for i in range(n):
            if not checkRow(i):
                return False
        
        # check each col
        for i in range(n):
            if not checkCol(i):
                return False
        
        # check each 3by3
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if not check3by3(i, j):
                    return False
        
        return True