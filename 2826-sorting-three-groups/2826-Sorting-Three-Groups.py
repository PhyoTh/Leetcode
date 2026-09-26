class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def solve(index: int, last: int) -> int:
            if (index, last) in cache:
                return cache[(index, last)]
            elif index == n:
                return 0
            
            keep_cost = solve(index + 1, nums[index]) if nums[index] >= last else float('inf')
            remove_cost = solve(index + 1, last) + 1
            cache[(index, last)] = min(keep_cost, remove_cost)
            return cache[(index, last)]

        return solve(0, 0)