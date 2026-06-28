1from collections import Counter
2class Solution:
3    def checkInclusion(self, s1: str, s2: str) -> bool:
4        n = len(s1)
5        if n > len(s2):
6            return False
7
8        s1_dict = Counter(s1)
9        s2_dict = {}
10        for i in range(n):
11            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
12
13        left, right = 0, n
14        while right < len(s2):
15            if s1_dict == s2_dict:
16                return True
17            s2_dict[s2[left]] -= 1
18            if s2_dict[s2[left]] == 0:
19                del s2_dict[s2[left]]
20            left += 1
21            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1
22            right += 1
23
24        return s1_dict == s2_dict