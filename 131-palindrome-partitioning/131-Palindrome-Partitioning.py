class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            if i + 1 < n:
                dp[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n):
                if i + length - 1 >= n:
                    continue
                dp[i][i + length - 1] = (s[i] == s[i + length - 1] and dp[i + 1][i + length - 2])
        
        # def is_palindrome(substring: str) -> bool:
        #     left, right = 0, len(substring) - 1
        #     while left <= right:
        #         if substring[left] != substring[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True

        result = []
        def backtrack(start: int, combinations: list):
            if start == n:
                result.append(combinations[:])
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    combinations.append(s[start: end + 1])
                    backtrack(end + 1, combinations)
                    combinations.pop()
        
        backtrack(0, [])
        return result