class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        for start, end in intervals:
            if end < newInterval[0]:
                result.append([start, end])
            elif newInterval[1] < start:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append([start, end])
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        if not inserted:
            result.append(newInterval)
        return result