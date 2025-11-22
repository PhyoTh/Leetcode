class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = 0
        start_index = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                start_index = i
                break

        for i in range(start_index, len(nums)-1):
            if nums[i+1] == 1:
                if counter < k:
                    return False
                counter = 0
            else:
                counter += 1
        return True