class Solution(object):
    # approach: sliding + binary search
    def characterReplacement(self, s, k):
        low = 1 # assume that we can def make a character long because len(s)>=1
        high = len(s) + 1 # just because we started at low=1, and longest is high-low
        while low + 1 < high:
            # have to add low,cuz low start anywhere
            mid = low + ((high - low) // 2)

            # check if we can make valid substring with the length of #mid
            if self.canMakeValidSubstring(s, k, mid):
                low = mid # true: current min length of substring, find larger
            else:# false: couldn't find any with that mid length, have to trim window
                high = mid 

        return low

    def canMakeValidSubstring(self, s, k, mid):
        freq_map = {} # to keep track of fixed letter and changable letters
        max_freq = 0
        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
        
            # if its bigger than #mid window, then slide right
            if end - start + 1 > mid: 
                freq_map[s[start]] -= 1 # before sliding remember to update freq_map
                start += 1

            max_freq = max(max_freq, freq_map[s[end]]) # this is the fix letter
            if mid - max_freq <= k: # there is a valid substring with #k replacements
                return True

        return False # couldn't find any valid substring:(