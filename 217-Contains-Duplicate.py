class Solution(object):
    def containsDuplicate(self, nums):
        searched_nums = set()
        for num in nums:
            if num in searched_nums:
                return True
            searched_nums.add(num)
        return False
        