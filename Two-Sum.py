class Solution(object):
    def twoSum(self, nums, target):
        save_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in save_nums:
                return [save_nums[diff], i]
            save_nums[num] = i