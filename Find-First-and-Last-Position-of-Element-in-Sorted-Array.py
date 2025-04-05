class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums , target, findleft):
            left = 0
            right = len(nums) - 1
            index = -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    index = mid
                    if findleft:
                        right = mid - 1
                    else:
                        left = mid + 1
            return index

        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)
        return [left, right]