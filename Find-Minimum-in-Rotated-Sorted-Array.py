class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        if len(nums) == 1 or nums[left] < nums[right]: # already sorted
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[left]: # inflection point is on the right
                left = mid + 1
            else:
                right = mid - 1