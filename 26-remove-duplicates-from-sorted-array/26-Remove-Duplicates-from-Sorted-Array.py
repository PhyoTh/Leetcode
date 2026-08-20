class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        seen = set()

        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            result.append(num)
        
        for i in range(len(result)):
            nums[i] = result[i]
        
        return len(result)