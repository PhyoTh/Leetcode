1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        n = len(nums)  
4        max_dp = [0] * n
5        min_dp = [0] * n
6
7        # base cases
8        max_dp[0] = nums[0]
9        min_dp[0] = nums[0]
10
11        largest = nums[0]
12        for i in range(1, n):
13            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
14            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
15            largest = max(largest, max_dp[i], min_dp[i])
16
17        return largest