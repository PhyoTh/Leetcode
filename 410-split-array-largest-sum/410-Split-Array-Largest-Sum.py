class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        result = right

        def valid(target: int) -> bool:
            subarrays = 1
            total = 0
            for num in nums:
                total += num
                if total > target:
                    subarrays += 1
                    total = num
            return subarrays <= k
        
        while left <= right:
            mid = (left + right) // 2

            if valid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result