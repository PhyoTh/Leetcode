class Solution(object):
    def threeSum(self, nums):
        # 2 pointer approach
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i-1]:
                self.twoSumII(nums, i, res)
        return res

    
    def twoSumII(self, nums, i, res):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            check = nums[i] + nums[low] + nums[high]
            if check < 0:
                low += 1
            elif check > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1