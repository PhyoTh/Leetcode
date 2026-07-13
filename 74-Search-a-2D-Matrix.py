class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        top, bottom = 0, n
        while top < bottom: # O(log n)
            pivot = (top + bottom) // 2

            if matrix[pivot][0] <= target <= matrix[pivot][m - 1]: # found
                break
            elif matrix[pivot][0] < target:
                top = pivot + 1
            elif matrix[pivot][0] > target:
                bottom = pivot
        
        left, right = 0, m
        while left < right: # O(log m)
            mid = (left + right) // 2

            if matrix[pivot][mid] == target:
                return True
            elif matrix[pivot][mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return False