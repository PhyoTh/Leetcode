from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq_map = Counter(s) # O(n)
        orders = sorted([(-freq, ch) for ch, freq in freq_map.items()])

        if -orders[0][0] > (n + 1) // 2:
            return ""
        
        result = ["" for _ in range(n)]
        index = 0
        for _, ch in orders:
            for _ in range(freq_map[ch]):
                result[index] = ch
                index += 2
                if index >= n:
                    index = 1
        
        return ''.join(result)