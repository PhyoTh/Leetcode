class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        sum_track = {0:1} # dictionary to keep track of how many times can you make up to a sum using different combination o elements
        count = 0 # counter for # of subarrays
        for x in nums:
            curr_sum += x
            find = curr_sum - k
            if find in sum_track:
                count += sum_track[find]
            sum_track[curr_sum] = sum_track.get(curr_sum, 0) + 1
        return count