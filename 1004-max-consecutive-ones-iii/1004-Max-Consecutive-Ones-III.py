class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:      
        result = 0
        zero_count = 0

        start = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            
            result = max(result, end - start + 1)
        return result