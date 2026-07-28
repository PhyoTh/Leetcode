class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        def is_palindrome(substring: str) -> bool:
            left, right = 0, len(substring) - 1
            while left <= right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int, combinations: list):
            if start == n:
                result.append(combinations[:])
                return
            
            for end in range(start + 1, n + 1):
                substring = s[start: end]
                if is_palindrome(substring):
                    combinations.append(substring)
                    backtrack(end, combinations)
                    combinations.pop()
        
        backtrack(0, [])
        return result