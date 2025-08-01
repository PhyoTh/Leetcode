class Solution(object):
    def threeSumSmaller(self, nums, target):
        counter = 0
        nums.sort()

        for i in range(len(nums)):
            # early break: if the target is negative and 
            # the sorted array starts with positive
            # it's impossible to get the sum of negative value
            if target <= 0 and nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < target:
                    counter += right - left
                    left += 1
                else:
                    right -= 1
                        
        return counter