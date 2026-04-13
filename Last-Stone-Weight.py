1class Solution:
2    # brute-force, N^2
3    import bisect
4    def lastStoneWeight(self, stones: List[int]) -> int:
5        stones.sort() # nlogn
6
7        while len(stones) > 1: # n (worst case: O(15))
8            t1, t2 = stones.pop(), stones.pop()
9            t3 = t1 - t2
10            bisect.insort(stones, t3)
11        return stones[0]
12    
13