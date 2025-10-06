class Solution(object):
    import heapq
    '''
    ans: ade, adf, bde, bdf, cde, cdf

    "{a, b, c} d {e, f}" 
      |
    0: [a, b, c]
    1: [d]
    2: [e, f]

    res = [a, b, c]
    res = [ad, bd, cd]
    res = [ade, bde, cde, adf, bdf, cdf]
    '''
    def expand(self, s):
        res = [""]

        i = 0
        while i < len(s):
            if s[i] == "{":
                i += 1 # skip '{'
                
                # collect all the options in sorted manner
                options = []
                while i < len(s) and s[i] != "}":
                    if s[i] != ",":
                        options.append(s[i])
                    i += 1
                    options.sort()
                
                i += 1 # skip '}'
            else:
                options = [s[i]]
                i += 1
            
            new_res = []
            for word in res:
                for option in options:
                    new_res.append(word+option)
            new_res.sort()
            res = new_res
        return res