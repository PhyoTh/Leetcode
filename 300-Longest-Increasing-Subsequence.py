class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]

        result = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
            result = max(result, dp[i])
        
        return result