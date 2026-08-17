from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums) # O(N)
        heap = []
        for num, count in nums_counter.items():
            if len(heap) == k:
                if count > heap[0][0]:
                    heapq.heappushpop(heap, (count, num))
                continue
            heapq.heappush(heap, (count, num))
        
        result = []
        for _, num in heap:
            result.append(num)
        return result