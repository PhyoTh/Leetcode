class TimeMap:
    def __init__(self):
        self.dict = {} # (key, value:[(timestamp, value), ... -> increasing order])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []

        # we don't need heapq or bisect.insort() cuz everytime set() is called, timestamp is increased
        self.dict[key].append((timestamp, value)) # O(1)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ''
        
        if timestamp > self.dict[key][-1][0]:
            return self.dict[key][-1][1]
        
        '''
        [0, 2, 4, 6, 8]
        timestamp = 3
        timestmap = 7
        '''
        closest = (timestamp, '')
        left, right = 0, len(self.dict[key])
        while left < right:
            mid = (left + right) // 2

            if self.dict[key][mid][0] == timestamp:
                return self.dict[key][mid][1]
            elif self.dict[key][mid][0] > timestamp:
                right = mid
            else:
                closest = self.dict[key][mid] if self.dict[key][mid][0] < closest[0] else closest
                left = mid + 1
        return closest[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)