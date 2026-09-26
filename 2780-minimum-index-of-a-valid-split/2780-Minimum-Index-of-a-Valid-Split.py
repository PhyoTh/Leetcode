from collections import Counter, defaultdict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right_split = defaultdict(int)
        left_split = defaultdict(int)

        dominant = None
        for num in nums: # O(n)
            right_split[num] += 1
            if right_split[num] * 2 > len(nums):
                dominant = num
        
        for i in range(len(nums) - 1): # O(n)
            left_split[nums[i]] += 1
            right_split[nums[i]] -= 1
            if right_split[nums[i]] == 0:
                del right_split[nums[i]]

            if dominant in left_split and dominant in right_split and left_split[dominant] * 2 > i + 1 and right_split[dominant] * 2 > len(nums) - (i + 1):
                return i
        
        return -1