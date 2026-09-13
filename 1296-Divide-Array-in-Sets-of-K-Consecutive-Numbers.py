from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        nums.sort()
        numCount = Counter(nums)
        for num in nums:
            if numCount[num] == 0:
                continue

            make = num
            count = 0
            while numCount[make] > 0 and count < k:
                numCount[make] -= 1
                count += 1
                make += 1
            
            if count != k:
                return False
        return True