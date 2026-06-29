1from collections import Counter
2class Solution:
3    def minWindow(self, s: str, t: str) -> str:
4        t_dict = Counter(t) # O(n)
5        smallest = None # (start, end)
6
7        s_dict = {}
8        seen_unique_chars = 0 # only increment if unique chars in t_dict count match
9        left = 0
10        for right in range(len(s)): # O(n)
11            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
12            if s[right] in t_dict.keys() and s_dict[s[right]] == t_dict[s[right]]:
13                seen_unique_chars += 1
14
15            # hit the unique chars, then you need to search min substring
16            while seen_unique_chars == len(t_dict):
17                if smallest is None:
18                    smallest = (left, right + 1)
19                if right - left + 1 < smallest[1] - smallest[0]:
20                        smallest = (left, right + 1)
21
22                s_dict[s[left]] -= 1
23                if s[left] in t_dict and s_dict[s[left]] < t_dict[s[left]]:
24                    seen_unique_chars -= 1
25
26                if s_dict[s[left]] == 0:
27                    del s_dict[s[left]]
28                left += 1
29        
30        return s[smallest[0]:smallest[1]] if smallest else ""