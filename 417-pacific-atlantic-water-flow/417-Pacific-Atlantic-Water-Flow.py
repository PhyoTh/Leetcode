from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        
        que = deque()
        visited = set()
        for col in range(m):
            que.append((0, col))
            visited.add((0, col))
        for row in range(1, n):
            que.append((row, 0))
            visited.add((row, 0))
        
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()
                
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    n_row, n_col = row + x, col + y
                    if not (0 <= n_row < n and 0 <= n_col < m) or (n_row, n_col) in visited or heights[n_row][n_col] < heights[row][col]:
                        continue
                    
                    que.append((n_row, n_col))
                    visited.add((n_row, n_col))
        
        result = []
        seen = set()
        for col in range(m):
            que.append((n-1, col))
            if (n-1, col) in visited:
                result.append([n-1, col])
            seen.add((n-1, col))
        for row in range(n-1):
            que.append((row, m-1))
            if (row, m-1) in visited:
                result.append([row, m-1])
            seen.add((row, m-1))
        
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()
                
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    n_row, n_col = row + x, col + y
                    if not (0 <= n_row < n and 0 <= n_col < m) or (n_row, n_col) in seen or heights[n_row][n_col] < heights[row][col]:
                        continue
                    
                    if (n_row, n_col) in visited:
                        result.append([n_row, n_col])
                    
                    que.append((n_row, n_col))
                    seen.add((n_row, n_col))
        
        return result
