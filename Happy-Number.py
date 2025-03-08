class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(n):
            return sum(int(digit) ** 2 for digit in str(n))
        
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = get_sum(n)
        return False