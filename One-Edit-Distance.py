class Solution(object):
    def isOneEditDistance(self, s, t):
        # edge cases
        if s == t: # if the two strings are same, no operations needed
            return False

        if len(s) > len(t):
            longer_s, shorter_s = s, t
        else:
            longer_s, shorter_s = t, s
        
        if len(longer_s) - len(shorter_s) > 1: # not possible with one edit
            return False
        
        long_walker = 0
        short_walker = 0
        found_edit = False # trigger this: when one extra char, when chars don't match, need one char
        while short_walker < len(shorter_s) and long_walker < len(longer_s):
            if longer_s[long_walker] == shorter_s[short_walker]:
                long_walker += 1
                short_walker += 1
                continue

            if found_edit:
                return False
        
            '''
            acb | ab
            ab | ac
            ab | abc
            '''
            if len(longer_s) == len(shorter_s):
                long_walker += 1
                short_walker += 1
            elif long_walker + 1 < len(longer_s) and longer_s[long_walker + 1] == shorter_s[short_walker]:
                long_walker += 1
            found_edit = True

        return found_edit or (len(longer_s) == len(shorter_s) + 1)