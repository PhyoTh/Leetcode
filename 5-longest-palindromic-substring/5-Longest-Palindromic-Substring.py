class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left: int, right: int) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        result = (0, 0)
        for i in range(n):
            odd_length = expand(i, i)
            dist = odd_length // 2
            result = (i - dist, i + dist) if odd_length > result[1] - result[0] + 1 else result

            even_length = expand(i, i + 1)
            dist = even_length // 2 - 1
            result = (i - dist, i + 1 + dist) if even_length > result[1] - result[0] + 1 else result
        
        return s[result[0]: result[1] + 1]