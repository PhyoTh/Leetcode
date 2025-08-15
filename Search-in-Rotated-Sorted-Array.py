class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print("left:", nums[left], " mid:", nums[mid], " right:", nums[right],)

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # left half is sorted
                if nums[left] <= target < nums[mid]: # target is in left-half
                    right = mid - 1
                else: # target is in right-half
                    left = mid + 1
            else: # right half is sorted
                if nums[mid] < target <= nums[right]: # target is in right-half
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
        