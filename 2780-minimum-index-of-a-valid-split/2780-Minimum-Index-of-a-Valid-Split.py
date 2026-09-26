from collections import Counter, defaultdict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        dominant = None
        count = 0
        for num in nums:
            if count == 0:
                dominant = num
            count += 1 if num == dominant else -1
        
        right_count = 0
        for num in nums:
            if num == dominant:
                right_count += 1
        
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
                right_count -= 1
            
            if left_count * 2 > i + 1 and right_count * 2 > n - (i + 1):
                return i
        return -1