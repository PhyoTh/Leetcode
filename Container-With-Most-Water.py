class Solution(object):
    def maxArea(self, height):
        # trick: is to move the pointers so that it finds the biggest height
        # while shirking down the width
        res = 0
    
        left = 0
        right = len(height) - 1
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))

            if height[left] > height [right]:
                right -= 1 
            else:
                left += 1
    
        return res