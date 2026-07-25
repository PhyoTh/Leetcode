class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []

        result = []
        def backtrack(start: int, combination: list):
            if sum(combination) > target:
                return
            elif sum(combination) == target:
                result.append(combination[:])
            
            for i in range(start, n):
                combination.append(candidates[i])
                backtrack(i, combination)
                combination.pop()
        
        backtrack(0, [])
        return result