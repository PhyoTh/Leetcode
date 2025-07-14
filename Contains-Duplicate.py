class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums) # this will elimate all the duplicate numbers
        return len(nums) != len(nums_set)