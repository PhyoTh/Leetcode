'''
[1, 2, 3, 4]
[2, 5, 7]
[1, 2, 2, 3, 4, 5, 7] -> 7, half = 3
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        
        half = (n1 + n2) // 2
        l, r = 0, n2
        while l <= r:
            m = (l + r) // 2
            remaining = half - m

            left1 = nums1[remaining - 1] if remaining > 0 else float('-inf')
            right1 = nums1[remaining] if remaining < n1 else float('inf')
            left2 = nums2[m - 1] if m > 0 else float('-inf')
            right2 = nums2[m] if m < n2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                break
            elif left2 > right1:
                r = m
            else:
                l = m + 1
        
        if (n1 + n2) % 2 == 0:
            result = (max(left1, left2) + min(right1, right2)) / 2
        else:
            result = min(right1, right2)
        
        return result