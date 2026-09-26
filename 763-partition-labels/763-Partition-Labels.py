from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        char_freq = Counter(s)
        window_freq = {}
        unique = 0
        result = []

        start = 0
        for end in range(len(s)): # O(n)
            unique += 1 if s[end] not in window_freq else 0
            window_freq[s[end]] = window_freq.get(s[end], 0) + 1

            if window_freq[s[end]] == char_freq[s[end]]:
                unique -= 1
            
            if unique == 0:
                result.append(end - start + 1)
                start = end + 1
                window_freq = {}

        return result