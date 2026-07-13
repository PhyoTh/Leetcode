class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]

        for i in range(n):
            if i + 1 < n:
                result[i + 1] *= result[i] * nums[i]
        
        postfix_sum = 1
        for i in range(n - 1, -1, -1):
            postfix_sum *= nums[i]
            if i - 1 >= 0:
                result[i - 1] *= postfix_sum
        
        return result