1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        sorted_intervals = sorted(intervals, key=lambda x:(x[0], x[1]))
4        result = [] 
5
6        prev_start = -1
7        prev_end = -1
8        for interval in sorted_intervals:
9            if prev_end >= interval[0]: # merge 
10                if interval[1] > prev_end:# expand
11                    prev_end = interval[1]
12            else: # not merge
13                if prev_start >= 0 and prev_end >= 0:
14                    result.append([prev_start, prev_end])
15                prev_start = interval[0]
16                prev_end = interval[1]
17        if prev_start >= 0 and prev_end >= 0:
18            result.append([prev_start, prev_end])
19        return result