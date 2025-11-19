class Solution:
    '''
        [73, 74, 75, 71, 69, 72, 76, 73]
                      |
        stack [73, 76, 72, 69]
        answer [0,0,0,0,1,1,0,0]
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        mono_stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while mono_stack and temperatures[mono_stack[-1]] <= temperatures[i]:
                mono_stack.pop()
            
            answer[i] = 0 if not mono_stack else mono_stack[-1] - i
            mono_stack.append(i)
        return answer