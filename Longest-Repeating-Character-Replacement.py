class Solution(object):
    def characterReplacement(self, s, k):
        # sliding window fast
        # keep in mind that max_window never shrinks, it only grows to
        # end - start + 1, and we move end / start pointers according to the 
        # max_freq we have seen through out the whole string
        max_window = 0 

        freq_map = {}
        max_freq = 0

        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            # important note: this is max_freq we have seen in any window
            max_freq = max(max_freq, freq_map[s[end]])

            if end-start+1 - max_freq > k:
                freq_map[s[start]] -= 1
                start += 1

            max_window = end - start + 1
            
        return max_window