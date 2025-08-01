class Solution(object):
    def threeSumClosest(self, nums, target):
        closestSum = float('inf')
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                # update if the closer one is found
                if abs(threeSum - target) < abs(closestSum - target): 
                    closestSum = threeSum

                # 3 conditions: 
                # if the sum is smaller that means you need bigger sum
                # if the sum is bigger that means you need smaller sum
                # else you found the sum that's your target
                if threeSum < target: 
                    left += 1
                elif threeSum > target:
                    right -= 1
                else:
                    return target
                    
        return closestSum