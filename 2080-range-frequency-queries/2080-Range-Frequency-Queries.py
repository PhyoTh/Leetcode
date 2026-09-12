import bisect
from collections import defaultdict
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.pos_map = defaultdict(list)
        for i in range(len(arr)):
            self.pos_map[arr[i]].append(i)
        
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos_map:
            return 0

        l = bisect.bisect_left(self.pos_map[value], left) # O(log n)
        r = bisect.bisect_right(self.pos_map[value], right) # O(log n)
        return r - l

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)