1class Solution:
2    def removeDuplicates(self, s: str, k: int) -> str:
3        stack = []
4
5        i = 0
6        while i < len(s):
7            if i == 0 or s[i] != s[i - 1]:
8                stack.append(1)
9            else:
10                stack[-1] += 1
11                if stack[-1] == k:
12                    stack.pop()
13                    s = s[:i - k + 1] + s[i + 1:]
14                    i = i - k
15            i += 1
16        return s