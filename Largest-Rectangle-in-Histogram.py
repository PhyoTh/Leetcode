1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = [(0, heights[0])] # (index, height)
4        largest = heights[0]
5
6        for i in range(1, len(heights)):
7            prev_index = None
8            while stack and heights[i] < stack[-1][1]:
9                prev_index, prev_height = stack.pop()
10                largest = max((i - prev_index) * prev_height, largest)
11
12            stack.append((i if prev_index == None else prev_index, heights[i]))
13        
14        while stack:
15            p_index, p_height = stack.pop()
16            width = len(heights) - p_index
17            largest = max(largest, width * p_height)
18
19        return largest