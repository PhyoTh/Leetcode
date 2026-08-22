class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cache = {}

        def backtrack(start: int, split: int) -> int:
            if split == 1:
                return sum(nums[start:])
            if (start, split) in cache:
                return cache[(start, split)]
            
            cur_sum, min_result = 0, float('inf')
            for i in range(start, n - split + 1):
                cur_sum += nums[i]
                max_sum = max(cur_sum, backtrack(i + 1, split - 1))
                min_result = min(min_result, max_sum)

                if cur_sum > min_result:
                    break

            cache[(start, split)] = min_result
            return min_result
        
        return backtrack(0, k)