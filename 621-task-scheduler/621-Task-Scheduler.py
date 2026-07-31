from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        tasks_counter = Counter(tasks)
        for task, count in tasks_counter.items():
            heapq.heappush(heap, -count)

        timer = 0
        que = deque()
        while heap or que:
            if heap:
                count = heapq.heappop(heap)
            timer += 1

            if -(count + 1) > 0:
                que.append((count + 1, timer + n))
            
            if que and que[0][1] == timer:
                count, _ = que.popleft()
                heapq.heappush(heap, count)
            count = 0

        return timer