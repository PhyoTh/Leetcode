class Solution:
    '''
    [0, 1, 2, 3, 4]
    [1, 2, 3, 4, 0]
    [4, 0, 1, 2, 3]
    '''
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[right]:
                pivot = left
                break
            elif nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid

        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            pivoted_mid = (pivot + mid) % n

            if nums[pivoted_mid] == target:
                return pivoted_mid
            elif nums[pivoted_mid] > target:
                right = mid
            else:
                left = mid + 1

        return -1