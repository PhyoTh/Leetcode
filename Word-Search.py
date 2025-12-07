1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        m = len(board)
4        n = len(board[0])
5
6        def hasWord(row, col, word, visited):
7            if len(word) == 0:
8                return True
9
10            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # right down left top
11                dx, dy = row + x, col + y
12                if 0 <= dx < m and 0 <= dy < n:
13                    if (dx, dy) not in visited and board[dx][dy] == word[0]:
14                        visited.add((dx, dy))
15                        if hasWord(dx, dy, word[1:], visited):
16                            return True
17                        visited.remove((dx, dy))
18            return False
19
20        for i in range(m):
21            for j in range(n):
22                if board[i][j] == word[0] and hasWord(i, j, word[1:], set([(i, j)])):
23                    return True
24
25        return False