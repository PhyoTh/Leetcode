class Solution(object):
    def groupAnagrams(self, strs):
        dict_str = defaultdict(list) # dictionary which creates a list for every entry
        for s in strs:
            sorted_str = ''.join(sorted(s)) # sorted returns list of characters in sorted order, and concatanting with string
            dict_str[sorted_str].append(s) # 
        return list(dict_str.values())