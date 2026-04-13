1class Solution:
2    import heapq
3    def lastStoneWeight(self, stones: List[int]) -> int:
4        for i in range(len(stones)): # n
5            stones[i] *= -1
6        heapq.heapify(stones)
7
8        while len(stones) > 1: # n
9            t1, t2 = heapq.heappop(stones), heapq.heappop(stones) # logn
10            t3 = t1 - t2
11            if t3 != 0:
12                heapq.heappush(stones, t3)
13        
14        return -1 * heapq.heappop(stones) if stones else 0
15    