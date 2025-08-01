class Solution(object):
    def threeSum(self, nums):
        # practice
        res = []
        nums.sort()

        for i in range(len(nums)):
            # early break case: if there is no neg, then impossible to get to zero
            if nums[i] > 0: 
                break
            elif i == 0 or nums[i] != nums[i-1]: # 1st loop or skip pivot duplicates 
                # 2pointer operation to find 3sum
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    threeSum = nums[i] + nums[left] + nums[right]
                    if threeSum < 0:
                        left += 1
                    elif threeSum > 0:
                        right -= 1
                    else:
                        res.append([nums[i], nums[left], nums[right]])
                        # these are just optimizations purpose, not really needed
                        # to skip the inner dups
                        while left + 1 < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right - 1 and nums[right] == nums[right-1]:
                            right -= 1
                        # you need to move both of the pointers regardless 
                        # because you want all the unqie pair of left and right
                        # corresponding to the pivot pointer
                        left += 1
                        right -= 1
        return res