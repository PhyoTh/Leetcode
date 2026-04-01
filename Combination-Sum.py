1class Solution:
2    '''
3    candidates = [2, 3, 6, 7]
4
5    stack = [], remaining = 7
6        stack = [2], remaining = 5
7            stack = [2, 2], remaining = 3
8                stack = [2, 2, 2], remaining = 1
9                    stack = [2, 2, 2, 2], remaining = -1
10                    stack = [2, 2, 2, 3], remaining = -2
11                    stack = [2, 2, 2, 6], remaining = -5
12                    stack = [2, 2, 2, 7], remaining = -6
13                stack = [2, 2, 3], remaining = 0
14                stack = [2, 3, 2], remaining = 0
15    '''
16    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
17        result = []
18        def rollout(stack: List[int], remaining: int, start: int):
19            if remaining == 0:
20                result.append(stack.copy())
21                return
22            elif remaining < 0:
23                return
24
25            for index, candidate in enumerate(candidates[start:]):
26                stack.append(candidate)
27                rollout(stack, remaining - candidate, start + index)
28                stack.pop()
29
30        rollout([], target, 0)
31        return result