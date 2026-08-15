class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        candidates.sort()

        def backtrack(start: int, combinations: List[int], remaining: int) -> None:
            if remaining < 0:
                return
            elif remaining == 0:
                result.append(combinations[:])
                return
            
            for i in range(start, n):
                if i > 0 and i != start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                
                combinations.append(candidates[i])
                backtrack(i + 1, combinations, remaining - candidates[i])
                combinations.pop()
            
        backtrack(0, [], target)
        return result
            