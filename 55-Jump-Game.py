class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lowest = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lowest:
                lowest = i
        
        return lowest == 0