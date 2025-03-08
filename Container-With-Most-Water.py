class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_area = 0

        def get_area(height: List[int], low: int, high: int) -> int:
            return min(height[low], height[high]) * (high - low)

        while low < high:
            curr_area = get_area(height, low, high)
            max_area = max(max_area, curr_area)

            # determine if we should increment low or decrement high
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area
