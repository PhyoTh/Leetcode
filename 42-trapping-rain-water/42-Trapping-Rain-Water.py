class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max <= right_max:
                left += 1
                result += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
            else:
                right -= 1
                result += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
        return result