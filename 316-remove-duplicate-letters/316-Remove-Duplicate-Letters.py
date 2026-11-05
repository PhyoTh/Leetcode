from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq_map = Counter(s)
        seen = set()
        stack = []
        
        for ch in s:
            freq_map[ch] -= 1

            if ch in seen:
                continue
            
            while stack and stack[-1] > ch and freq_map[stack[-1]] > 0:
                seen.remove(stack[-1])
                stack.pop()
            
            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)