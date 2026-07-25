class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        if n == 0:
            return []

        candidates.sort()
        result = []
        def backtrack(start: int, combination: list, remaining: int):
            if remaining == 0:
                result.append(combination[:])
            
            visited = set()
            for i in range(start, n):
                if candidates[i] in visited:
                    continue
                visited.add(candidates[i])

                if remaining - candidates[i] < 0:
                    break
                
                combination.append(candidates[i])
                backtrack(i + 1, combination, remaining - candidates[i])
                combination.pop()
        
        backtrack(0, [], target)
        return result