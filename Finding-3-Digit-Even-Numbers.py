1class Solution:
2    def findEvenNumbers(self, digits: List[int]) -> List[int]:
3        # brute force is O(n^3) not efficient
4        from collections import Counter
5        freq = Counter(digits)
6        result = []
7
8        for i in range(100, 1000, 2): # this will only consist of non-zero leading, unique 3-digits even numbers
9            d1, d2, d3 = i // 100, (i // 10) % 10, i % 10
10            cur_freq = Counter([d1, d2, d3])
11            if all(cur_freq[d] <= freq[d] for d in cur_freq):
12                result.append(i)
13        return result