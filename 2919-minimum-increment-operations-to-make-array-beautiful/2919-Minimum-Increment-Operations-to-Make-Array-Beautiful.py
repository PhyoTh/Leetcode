class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        first = max(0, k - nums[0])
        second = max(0, k - nums[1])
        third = max(0, k - nums[2])

        for i in range(3, n):
            fourth = max(0, k - nums[i]) + min(first, second, third)

            first = second
            second = third
            third = fourth
        return min(first, second, third)