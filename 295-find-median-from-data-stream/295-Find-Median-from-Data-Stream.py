import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    
    def balanceHeaps(self):
        diff = len(self.max_heap) - len(self.min_heap)

        if diff > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif diff < 0:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def addNum(self, num: int) -> None:
        if self.max_heap and num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        elif self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        self.balanceHeaps()

    def findMedian(self) -> float:
        total = len(self.max_heap) + len(self.min_heap)
        if total == 0:
            return 0
        
        return (-self.max_heap[0] + self.min_heap[0]) / 2 if total % 2 == 0 else -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()