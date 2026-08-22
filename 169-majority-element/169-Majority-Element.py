from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)
        major_element = (-1, -1)

        for num, count in nums_dict.items():
            if count > major_element[1]:
                major_element = (num, count)
        
        return major_element[0]