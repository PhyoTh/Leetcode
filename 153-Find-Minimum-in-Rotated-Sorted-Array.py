class Solution:
    '''
    [0, 1, 2, 3, 4]
    [4, 0, 1, 2, 3]
    [1, 2, 3, 4, 0]
    '''
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[right]:
                return nums[left]
            elif nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid

        return -1