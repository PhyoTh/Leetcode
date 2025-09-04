'''
candidates = [2, 3, 6, 7], target = 7
result = [[3, 2, 2]]

backtrack:
combination = [2], remain = 5, i = 0
combination = [2, 2], remain = 3, i = 0
combination = [2, 2, 2], remain = 1, i = 0
combiination = [2, 2, 2, 2], remain = -1, i = 0

combination = [3], remain = 4, i = 1 <= this is why you need to pop
combination = [3, 2], remain = 2, i = 0
combination = [3, 2, 2], remain = 0, i = 0
combiination = [3, 2, 2, 2], remain = -2, i = 0
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        self.result = []
        self.backtrack(target, candidates, [], 0)
        return self.result
    
    def backtrack(self, remain, candidates, combination, start):
        if remain == 0:
            # found ! then make a deep copy of current combination to the result
            self.result.append(list(combination)) 
            return
        elif remain < 0:
            return # exceeds the target,z    don't do anything
        
        for i in range(start, len(candidates)):
            # try out the first candidate
            combination.append(candidates[i])

            # try out this candidate with other candidates
            self.backtrack(remain - candidates[i], candidates, combination, i) 

            # pop it, so in the next iteration you can swap out with the next candidate
            combination.pop()