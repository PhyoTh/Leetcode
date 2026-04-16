1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        max_stone = max(stones)
4        counter = [0] * (max_stone + 1)
5
6        for stone in stones:
7            counter[stone] += 1
8        
9        biggest_stone = 0
10        curr_stone = max_stone
11        while curr_stone > 0:
12            if counter[curr_stone] == 0: # edge case when max is 0
13                curr_stone -= 1
14            # keep smashing until the most right curr stone, becomes count 1
15            elif biggest_stone == 0:
16                counter[curr_stone] %= 2
17                if counter[curr_stone] == 1:
18                    biggest_stone = curr_stone
19                curr_stone -= 1
20            else:
21                counter[curr_stone] -= 1
22                if biggest_stone - curr_stone <= curr_stone:
23                    counter[biggest_stone - curr_stone] += 1
24                    biggest_stone = 0
25                else:
26                    biggest_stone -= curr_stone
27        return biggest_stone