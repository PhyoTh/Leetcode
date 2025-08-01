class Solution(object):
    def threeSumSmaller(self, nums, target):
        # 2 pointer approach
        threeSumCount = 0
        nums.sort() # we need to sort this so we can satisfy i<j<k condition

        for i in range(len(nums)):
            # if target is negative, and the sorted array starts with positive
            # there is no possible tuple that will get to negative target
            if target <= 0 and nums[i] > 0: 
                break
            threeSumCount = self.twoSum(nums, i, target, threeSumCount)
        return threeSumCount
    
    def twoSum(self, nums, i, target, threeSumCount):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            check = nums[i] + nums[low] + nums[high]
            if check < target:
                # trick: because the high is at the highest max you can obtain
                # so even if you high -= 1, with the same i, and low
                # you [i] + [low] + [high] will still < target
                threeSumCount += (high - low)
                low += 1
            else:
                high -= 1 # sum is too big, need to reduce down
        return threeSumCount