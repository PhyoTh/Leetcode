class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        current_end = 0
        jumps = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = furthest

                if current_end >= len(nums) - 1:
                    break
        
        return jumps