class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        
        odd = True if n % 2 != 0 else False
        if n < 0:
            result = self.myPow(x, int(n / 2)) ** 2
            result *= 1/x if odd else 1
        else:
            result = self.myPow(x, n // 2) ** 2
            result *= x if odd else 1
        
        return result

        '''
        n = -10 -> -5 -> -2 -> -1
        1 -> 2.0
        2 -> 4.0
        5 -> 
        '''