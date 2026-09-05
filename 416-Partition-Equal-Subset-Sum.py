class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for index in range(target, num - 1, -1):
                dp[index] = dp[index] or dp[index - num]

        return dp[target]