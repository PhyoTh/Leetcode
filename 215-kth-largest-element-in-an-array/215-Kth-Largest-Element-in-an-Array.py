import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k and num > heap[0]:
                heapq.heappushpop(heap, num)
                continue

            if len(heap) < k:
                heapq.heappush(heap, num)
        return heap[0]