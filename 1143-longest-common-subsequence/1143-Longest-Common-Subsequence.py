from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)

        @lru_cache(maxsize=None)
        def topdown(p1: int, p2: int) -> int:
            if p1 == n1 or p2 == n2:
                return 0
            
            case1 = topdown(p1 + 1, p2)
            
            case2 = 0
            found = text2.find(text1[p1], p2)
            if found != -1:
                case2 = 1 + topdown(p1 + 1, found + 1)
            return max(case1, case2)
        
        return topdown(0, 0)