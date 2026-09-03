class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        n = len(nums)
        rob_first = [0 for _ in range(n - 1)]
        rob_first[0] = nums[0]
        rob_first[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            rob_first[i] = max(rob_first[i - 1], rob_first[i - 2] + nums[i])

        rob_last = [0 for _ in range(n - 1)]
        rob_last[0] = nums[1]
        rob_last[1] = max(nums[1], nums[2])
        for i in range(2, n - 1):
            rob_last[i] = max(rob_last[i - 1], rob_last[i - 2] + nums[i + 1])
        
        return max(rob_first[-1], rob_last[-1])