class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        
        result = []
        def backtrack(combinations: list, visited: set()):
            if len(combinations) == n:
                result.append(combinations[:])
                return
            
            for i in range(n):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])

                combinations.append(nums[i])
                backtrack(combinations, visited)
                combinations.pop()

                visited.remove(nums[i])
        
        backtrack([], set())
        return result