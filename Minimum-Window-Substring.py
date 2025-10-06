class Solution(object):
    def minWindow(self, s, t):
        min_window = (float("inf"), 0, 0) # (widow width, start, end)

        # current window
        curr_freq = {} # keep track of char count in current window
        curr_match_count = 0 # keep track of unique matched chars with target in current window

        # target
        from collections import Counter
        target_freq = Counter(t)
        unique_char_count = len(target_freq)
    
        start = 0
        for end in range(len(s)):
            curr_freq[s[end]] = curr_freq.get(s[end], 0) + 1

            if s[end] in target_freq and curr_freq[s[end]] == target_freq[s[end]]:
                curr_match_count += 1
            
            while curr_match_count == unique_char_count:
                if end-start+1 < min_window[0]: # current window smaller than the minimum recorded
                    min_window = (end-start+1, start, end)
                
                # move start window by 1
                if s[start] in target_freq and curr_freq[s[start]] == target_freq[s[start]]:
                    curr_match_count -= 1
                curr_freq[s[start]] -= 1
                start += 1

        return "" if min_window[0] == float("inf") else s[min_window[1] : min_window[2]+1]