class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        ans = [1] * length

        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in range(length - 2, -1, -1):
            right *= nums[i + 1]
            ans[i] *= right
            
        return ans