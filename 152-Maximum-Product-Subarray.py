class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]
        for i in range(1, len(nums)):
            cur_max = max_prod * nums[i]
            cur_min = min_prod * nums[i]

            max_prod = max(cur_max, nums[i], cur_min)
            min_prod = min(cur_max, nums[i], cur_min)
            result = max(result, max_prod)
        
        return result