class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False

        seen = {} # O(n)

        for i, num in enumerate(nums): # O(n)
            if num in seen and abs(i - seen[num]) <= k:
                return True
            
            seen[num] = i

        return False