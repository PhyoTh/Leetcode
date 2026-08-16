class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        result = []
        
        def backtrack(start: int, combinations: List[int], remaining: int):
            if remaining < 0:
                return
            elif len(combinations) == k:
                if remaining == 0:
                    result.append(combinations[:])
                return
            
            for i in range(start, 9):
                combinations.append(candidates[i])
                backtrack(i + 1, combinations, remaining - candidates[i])
                combinations.pop()
        
        backtrack(0, [], n)
        return result