class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks = 0 # this break will count whenever nums[i] > nums[i+1]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                breaks+=1
            if breaks > 1: # more than one non-increasing break
                return False
        if breaks == 0: # already sorted
            return True
        return nums[0] >= nums[-1] # if breaks = 1 then check if the first >= last
            