class Solution(object):
    def twoSum(self, nums, target):
        num_map = {} # hash map
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i] # find the complement in the prev stored map and return together with current

            num_map[num] = i # stores the indices of the numbers
        return []