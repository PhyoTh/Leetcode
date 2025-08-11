class Solution(object):
    ''' pay attention to how they check if the current window is valid
        # first, count the number of chars that we need to meet in order for substring to become valid
        # second, then increment "formed" counter when the condition of unique_char_count in current_window == required_char_count in t'''
    def minWindow(self, s, t):
        # unoptimized sliding minWindow
        if not s or not t:
            return ""

        min_window = (float("inf"), None, None) # (window_width, left ptr, right ptr)

        current_window_dict = {}
        formed_char_count = 0

        from collections import Counter
        dict_t = Counter(t) # to compare with the current window to check for validity
        required_char_count = len(dict_t) # to compare with formed_char_count

        # if substring is valid, move up start ptr to check if its stil valid
        # if substring is not valid, keep moving up end ptr to check if its valid 
        start = 0
        for end in range(len(s)):
            current_window_dict[s[end]] = current_window_dict.get(s[end], 0) + 1

            # look up to see if any of the unique char in t has been formed
            if s[end] in dict_t and current_window_dict[s[end]] == dict_t[s[end]]:
                formed_char_count += 1
            
            # if the current window is valid
            while start <= end and formed_char_count == required_char_count:
                if end-start+1 < min_window[0]: # check and update if its smallest
                    min_window = (end-start+1, start, end)
                
                if s[start] in dict_t and current_window_dict[s[start]] == dict_t[s[start]]:
                    formed_char_count -= 1
                current_window_dict[s[start]] -= 1
                start += 1
            
        return "" if min_window[0] == float("inf") else s[min_window[1]:min_window[2]+1]