class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_max = solve(left, mid)
            right_max = solve(mid + 1, right)
            
            left_sum = 0
            best_left = float('-inf')
            for i in range(mid, left - 1, -1):
                left_sum += nums[i]
                best_left = max(best_left, left_sum)

            right_sum = 0
            best_right = float('-inf')
            for i in range(mid + 1, right + 1):
                right_sum += nums[i]
                best_right = max(best_right, right_sum)

            return max(left_max, right_max, best_left + best_right)

        return solve(0, len(nums) - 1)