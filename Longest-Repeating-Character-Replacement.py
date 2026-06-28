1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        n = len(s)
4        counter = {}
5        longest = float('-inf')
6        max_freq = None
7
8        left = 0
9        for right in range(n):
10            counter[s[right]] = counter.get(s[right], 0) + 1
11            max_freq = max(counter.values())
12
13            while (right - left + 1) - max_freq > k:
14                counter[s[left]] -= 1
15                if counter[s[left]] == 0:
16                    del counter[s[left]]
17                max_freq = max(counter.values())
18                left += 1
19
20            longest = max(longest, right - left + 1)
21
22        return longest