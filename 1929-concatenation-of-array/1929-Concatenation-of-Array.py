class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(2 * n)]

        for i in range(2 * n):
            index = i % n
            result[i] = nums[index]
        return result