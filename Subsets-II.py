1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4
5        n = len(nums)
6        result = []
7
8        def backtrack(subset, start):
9            result.append(subset.copy())
10
11            for i in range(start, n):
12                if i > start and nums[i] == nums[i - 1]:
13                    continue
14
15                subset.append(nums[i])
16                backtrack(subset, i + 1)
17                subset.pop()
18            
19        backtrack([], 0)
20        return result