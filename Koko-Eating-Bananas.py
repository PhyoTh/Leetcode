class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = left + (right - left) // 2

            time_count = 0
            for pile in piles:
                time_count += math.ceil(pile / middle)
            
            if time_count <= h:
                right = middle
            else:
                left = middle + 1
        
        return right