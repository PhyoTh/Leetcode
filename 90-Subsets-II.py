class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]
        
        result = []
        nums.sort()
        def backtrack(start: int, combinations: list):
            result.append(combinations[:])

            visited = set()
            for i in range(start, n):
                if nums[i] in visited:
                    continue
                
                visited.add(nums[i])
                combinations.append(nums[i])
                backtrack(i + 1, combinations)
                combinations.pop()
        
        backtrack(0, [])
        return result