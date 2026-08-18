class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = float('inf')

        result = [0 for _ in range(m + n)]
        index = 0
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p2 == n or nums1[p1] <= nums2[p2]:
                result[index] = nums1[p1]
                p1 += 1
            elif p1 == m or nums1[p1] > nums2[p2]:
                result[index] = nums2[p2]
                p2 += 1
            
            index += 1
        
        for i in range(n + m):
            nums1[i] = result[i]