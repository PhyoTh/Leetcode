1import math
2class Solution:
3    def minEatingSpeed(self, piles: List[int], h: int) -> int:
4        result = max(piles)
5        left, right = 1, max(piles)
6        while left < right:
7            mid = (left + right) // 2
8
9            time = 0
10            for pile in piles:
11                time += math.ceil(pile / mid)
12
13            if time <= h:
14                result = min(result, mid)
15                right = mid
16            else:
17                left = mid + 1
18
19        return result