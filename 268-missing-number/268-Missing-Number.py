class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        real_sum = len(nums) * (len(nums) + 1) // 2
        cur_sum = sum(nums)
        return real_sum - cur_sum