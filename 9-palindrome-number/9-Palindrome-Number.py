import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        upper_x = x
        lower_x = x

        upper_bound = math.floor(math.log(x, 10))
        lower_bound = 1

        while upper_bound >= lower_bound:
            left = upper_x // (10 ** upper_bound)
            right = lower_x % (10 ** lower_bound)

            if left != right:
                return False

            upper_x -= left * (10 ** upper_bound)
            lower_x //= (10 ** lower_bound)
            upper_bound -= 1

        return True
        