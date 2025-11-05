class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        # left-top priority dfs rollout (recursive)
        def pacificRollOut(row, col, seen) -> bool:
            # check if row and col is touching, left or top
            if row == 0 or col == 0:
                return True
            
            seen.add((row, col))
            for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]: # top left bottom right
                new_row = row + i
                new_col = col + j
                if (new_row,  new_col) not in seen and 0 <= new_row < m and 0 <= new_col < n:
                    if heights[row][col] >= heights[new_row][new_col]:
                        if pacificRollOut(new_row, new_col, seen):
                            return True
            
            return False
        
        # right-bottom priority dfs rollout (recursive)
        def atlanticRollOut(row, col, seen) -> bool:
            if row == m-1 or col == n-1:
                return True
            
            seen.add((row, col))
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # bottom right top left 
                new_row = row + i
                new_col = col + j
                if (new_row,  new_col) not in seen and 0 <= new_row < m and 0 <= new_col < n:
                    if heights[row][col] >= heights[new_row][new_col]:
                        if atlanticRollOut(new_row, new_col, seen):
                            return True
            
            return False

        # main
        result = []
        for i in range(m):
            for j in range(n):
                if pacificRollOut(i, j, set()) and atlanticRollOut(i, j, set()):
                    result.append([i, j])
        return result