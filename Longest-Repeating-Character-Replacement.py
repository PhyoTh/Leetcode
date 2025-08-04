class Solution(object):
    def characterReplacement(self, s, k):
        # sliding window slow, without frequency map
        # this algorithm marks each unique char in the string as fixed 
        # like an idiodt and loop over each unique char
        letters_set = set(s) # so it only contains the unique chars without dups
        max_window = 0

        for letter in letters_set:
            count = 0
            start = 0 
            for end in range(len(s)):
                # count up the unique letter when expanding the end of window
                if s[end] == letter:
                    count += 1

                # end-start+1 = window
                # as long as window - fixed_letter_count is > k, we need to shrink
                while end-start+1 - count > k:
                    if s[start] == letter:
                        count -= 1
                    start += 1
                    
                max_window = max(max_window, end-start+1)
        
        return max_window