class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        if nums[0] > 0:
            return []
        
        result = []
        for left in range(len(nums)):
            if left > 0 and nums[left - 1] == nums[left]:
                continue

            mid, right = left + 1, len(nums) - 1

            while mid < right:
                total = nums[left] + nums[mid] + nums[right]

                if total == 0:
                    result.append([nums[left], nums[mid], nums[right]])

                    mid += 1
                    while mid < right and nums[mid - 1] == nums[mid]:
                        mid += 1
                    
                    right -= 1
                    while mid < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif total < 0:
                    mid += 1
                elif total > 0:
                    right -= 1
            
        return result