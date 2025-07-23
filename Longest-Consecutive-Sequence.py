class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # n-1 check to see if its the smallest
            # number in the sequence
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                longest = max(longest, length)
        
        return longest