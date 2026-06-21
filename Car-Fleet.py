1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = sorted(zip(position, speed), reverse=True) # closest -> furthest
4        stack = []
5        for position, speed in pairs:
6            time_to_target = (target - position) / speed
7            if stack and stack[-1] >= time_to_target: # join
8                continue
9            stack.append(time_to_target)
10
11        return len(stack)