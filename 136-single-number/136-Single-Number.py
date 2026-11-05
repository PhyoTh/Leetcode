class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        acc = 0
        for num in nums:
            acc ^= num
        return acc