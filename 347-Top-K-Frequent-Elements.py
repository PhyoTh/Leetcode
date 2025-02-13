class Solution(object):
    def topKFrequent(self, nums, k):
        res = []
        x = Counter(nums) # Count frequency of the string
        topK = x.most_common(k) # get the K most freequent elements
        for num, freq in topK:
                res.append(num)
        return res