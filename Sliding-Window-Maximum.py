1from collections import deque
2class Solution:
3    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
4        result = []
5        que = deque()
6
7        left = 0
8        for right in range(len(nums)):
9            while que and nums[que[-1]] <= nums[right]:
10                que.pop()
11            que.append(right)
12
13            if que[0] < left:
14                que.popleft()
15
16            if right - left + 1 == k:
17                result.append(nums[que[0]])
18                left += 1
19        
20        return result