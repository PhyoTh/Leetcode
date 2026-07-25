class Node:
    def __init__(self, val = ''):
        self.val = val
        self.end = False
        self.next = {}

class Solution:
    def __init__(self):
        self.root = Node()
    
    def buildTrie(self, word: str) -> None:
        walker = self.root

        for char in word:
            if char not in walker.next:
                walker.next[char] = Node(char)
            walker = walker.next[char]
        walker.end = True
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])

        for word in words:
            self.buildTrie(word)
        
        result = []
        def backtrack(row: int, col: int, root: Node, word: List[str], visited: set()):
            if root.end:
                root.end = False
                result.append(''.join(word))

            if len(root.next) == 0:
                return
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_row, n_col = row + x, col + y
                if not (0 <= n_row < n and 0 <= n_col < m) or (n_row, n_col) in visited:
                    continue
                
                visited.add((n_row, n_col))

                if board[n_row][n_col] in root.next:
                    word.append(board[n_row][n_col])
                    backtrack(n_row, n_col, root.next[board[n_row][n_col]], word[:], visited)
                    word = word[:-1]
                
                visited.remove((n_row, n_col))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in self.root.next:
                    backtrack(i, j, self.root.next[board[i][j]], [board[i][j]], set([(i, j)]))

        return result