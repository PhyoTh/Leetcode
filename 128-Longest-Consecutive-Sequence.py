class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(n)
        longest = 0

        for num in num_set: # O(n)
            if num - 1 not in num_set: # O(1)
                length = 0
                while num + length in num_set: # O(k)
                    length += 1
                    longest = max(longest, length)
        
        return longest