1from collections import Counter
2class Solution:
3    def checkInclusion(self, s1: str, s2: str) -> bool:
4        n = len(s1)
5        s1_dict = Counter(s1)
6        
7        left, right = 0, n
8        while right <= len(s2):
9            s2_dict = Counter(s2[left:right])
10            if s1_dict == s2_dict:
11                return True
12            left += 1
13            right += 1
14
15        return False