1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        current_sum = 0
4        original_sum = 0
5        for i in range(0, len(nums) + 1):
6            original_sum += i
7
8            if i < len(nums):
9                current_sum += nums[i]
10        return original_sum - current_sum