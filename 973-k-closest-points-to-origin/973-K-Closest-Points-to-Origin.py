import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        heap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            if len(heap) >= k:
                if distance < -heap[0][0]:
                    heapq.heappushpop(heap, (-distance, [x, y]))
            else:
                heapq.heappush(heap, (-distance, [x, y]))
        
        return [point for dis, point in heap]
        '''
        return heapq.nsmallest(k, points, key=lambda point: (point[0] ** 2) + (point[1] ** 2))