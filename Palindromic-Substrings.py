1class Solution:
2    # brute-force
3    # def isPalindrome(self, s:str) -> bool:
4    #     first = 0
5    #     last = len(s) - 1
6    #     while first <= last:
7    #         if s[first] != s[last]:
8    #             return False
9
10    #         first += 1
11    #         last -= 1
12    #     return True
13
14    # def countSubstrings(self, s: str) -> int:
15    #     count = 0
16    #     for i in range(0, len(s)):
17    #         for j in range(i, len(s)):
18    #             if self.isPalindrome(s[i:j+1]):
19    #                 count += 1
20    #     return count
21
22    # dp
23    def countSubstrings(self, s: str) -> int:
24        n = len(s)
25        if n == 0: return 0
26
27        count = 0
28        dp = [[False for _ in range(n)] for _ in range(n)]
29
30        # base case single letter
31        for i in range(n):
32            dp[i][i] = True
33            count += 1
34        
35        # base case double letter
36        for i in range(n - 1):
37            dp[i][i+1] = True if s[i] == s[i+1] else False
38            count += dp[i][i+1]
39        
40        # for all substrings >= 3 letter
41        for length in range(3, n + 1):
42            first = 0
43            last = first + length - 1
44            while last < n:
45                if s[first] == s[last] and dp[first + 1][last - 1]:
46                    dp[first][last] = True
47                    count += dp[first][last]
48
49                first += 1
50                last += 1
51
52        return count