class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return result
            result += char
        
        return result