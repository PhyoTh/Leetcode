class Solution(object):
    def groupAnagrams(self, strs):
        seen = collections.defaultdict(list) # this will return empty list if the given key is not present
        for s in strs:
            key = [0] * 26 # this is the seen(dict) key to keep track of the same anagrams
            for c in s:
                key[ord(c) - ord("a")] += 1 # treat ascii value as index
            seen[tuple(key)].append(s)
        return seen.values()
