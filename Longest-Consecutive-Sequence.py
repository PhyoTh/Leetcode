class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums) # change it to set for O(1) search
        longest = 0

        for n in nums_set:
            # Check if n is the smallest number in the sequence
            # i.e. if n - 1 is not present
            if n - 1 not in nums_set: 
                length = 1
                while (n+length) in nums_set: # this will count up to the longest sequence
                    length += 1
                
                longest = max(longest, length) # update the longest sequence count
        
        return longest