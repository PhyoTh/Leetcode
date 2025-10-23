class Solution(object):
    def singleNumber(self, nums):
        temp = 0
        for num in nums:
            temp = temp ^ num
        return temp