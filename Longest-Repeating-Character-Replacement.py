class Solution(object):
    def characterReplacement(self, s, k):
        max_window = 0

        freq_map = {}
        max_freq = 0

        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            max_freq = max(max_freq, freq_map[s[end]]) # this is all time max freq

            if end-start+1 - max_freq > k: # current window has > k replacements
                freq_map[s[start]] -= 1 # update the frequency
                start += 1 # move the window without shrinking

            max_window = end - start + 1 # max_window will be the current window because we didn't shrink
        
        return max_window