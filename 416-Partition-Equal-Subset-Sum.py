class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        
        if n == 1 or total % 2 != 0:
            return False
        
        half = total // 2
        cache = {}
        def backtrack(start: int, current_sum: int) -> bool:
            if (start, current_sum) in cache:
                return cache[(start, current_sum)]
            elif current_sum == half:
                return True
            elif current_sum > half or start == n:
                return False
            
            cache[(start, current_sum)] = backtrack(start + 1, current_sum + nums[start]) or backtrack(start + 1, current_sum)
            return cache[(start, current_sum)]
        
        return backtrack(0, 0)