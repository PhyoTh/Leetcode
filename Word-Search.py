class Solution(object):
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if word[0] == board[row][col] and self.hasWordOnBoard(board, row, col, 0, word):
                    return True

        return False

    def hasWordOnBoard(self, board, row, col, k, word):
        if len(word) == k:
            return True
        if not(0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] != word[k]:
            return False

        temp = board[row][col]
        board[row][col] = "#"

        found = (self.hasWordOnBoard(board, row - 1, col, k+1, word) or
                 self.hasWordOnBoard(board, row + 1, col, k+1, word) or 
                 self.hasWordOnBoard(board, row, col + 1, k+1, word) or 
                 self.hasWordOnBoard(board, row, col - 1, k+1, word))

        board[row][col] = temp
        return found