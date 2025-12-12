1class Solution:
2    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
3        count = 0
4        result = []
5        nums = [0] * n
6        for idx, color in queries:
7            prev = nums[idx - 1] if idx > 0 else 0
8            nxt = nums[idx + 1] if idx < n - 1 else 0
9            if nums[idx] != 0 and nums[idx] == prev: # remove pair with prev
10                count -= 1
11            if nums[idx] != 0 and nums[idx] == nxt: # remove pair with nxt
12                count -= 1
13            
14            nums[idx] = color
15
16            if nums[idx] != 0 and nums[idx] == prev: # add pair with prev
17                count += 1
18            if nums[idx] != 0 and nums[idx] == nxt: # add pair with nxt
19                count += 1
20            
21            result.append(count)
22        return result