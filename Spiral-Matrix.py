class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        direction = 1
        i, j = 0, -1  # initial pointer

        output = []
        while m * n > 0:
            for _ in range(n):  # move horizontally
                j += direction
                output.append(matrix[i][j])
            m -= 1
            for _ in range(m):  # move vertically
                i += direction
                output.append(matrix[i][j])
            n -= 1

            direction *= -1  # filp the direction
        return output
