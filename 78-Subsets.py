class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]

        result = []
        def backtrack(start: int, combination: list):
            result.append(combination[:])
            
            for i in range(start, n):
                combination.append(nums[i])
                backtrack(i + 1, combination)
                combination.pop()
        
        backtrack(0, [])
        return result