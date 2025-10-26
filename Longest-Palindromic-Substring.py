class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        # first fill up the length 1s
        for i in range(n):
            dp[i][i] = True

        # fill up length 2s
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # fill up length 3 and so on...
        for length in range(2, n):
            for start in range(n - length):
                end = start + length
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    ans = [start, end]

        i, j = ans
        return s[i:j + 1]
