class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for num in nums:
            if not tail or tail[-1] < num:
                tail.append(num)
            else:
                left, right = 0, len(tail)

                while left < right:
                    mid = (left + right) // 2

                    if tail[mid] >= num:
                        right = mid
                    else:
                        left = mid + 1
                
                tail[left] = num
        
        return len(tail)