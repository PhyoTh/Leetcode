class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            x = x // 10

            result = result * 10 + digit
            if result > 2**31-1:
                return 0
        return result * sign