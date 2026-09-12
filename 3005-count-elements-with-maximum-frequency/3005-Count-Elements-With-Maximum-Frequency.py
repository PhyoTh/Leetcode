from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num2freq = defaultdict(int)
        freqCount = defaultdict(int)
        max_freq = 0

        for num in nums:
            num2freq[num] += 1
            freqCount[num2freq[num]] += 1
            max_freq = max(max_freq, num2freq[num])

        return 0 if max_freq == 0 else max_freq * freqCount[max_freq]