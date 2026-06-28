1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        n, m = len(nums1), len(nums2)
4        total = n + m
5        half = total // 2
6
7        if n > m:
8            nums1, nums2 = nums2, nums1
9            n, m = m, n
10
11        left, right = 0, n
12        while left <= right:
13            mid = (left + right) // 2
14            remaining = half - mid
15
16            left1 = nums1[mid-1] if mid > 0 else float('-inf')
17            right1 = nums1[mid] if mid < n else float('inf')
18            left2 = nums2[remaining - 1] if remaining > 0 else float('-inf')
19            right2 = nums2[remaining] if remaining < m else float('inf')
20
21            if left1 <= right2 and left2 <= right1:
22                break
23            elif left1 > right2:
24                right = mid - 1
25            else:
26                left = mid + 1
27        
28        if total % 2 == 0:
29            result = (max(left1, left2) + min(right1, right2)) / 2
30        else:
31            result = min(right1, right2)
32        return result