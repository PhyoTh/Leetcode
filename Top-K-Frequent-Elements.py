class Solution(object):
    def topKFrequent(self, nums, k):
        # count the frequencies first, this step is unavoidable
        counter = {} 
        for num in nums: # O(n)
            counter[num] = counter.get(num, 0) + 1 

        # we will use index numbers as freq / e.g. three # of frequencies, we store in i-3th
        # the reason we need 2d-list is to be able to store the elements with same # of frequencies
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items(): # O(n)
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1): # this iterate thorugh freq from highest to lowest
            for n in freq[i]: # O(n) even tho its nested loop, we are only iterating up to "k" iterations
                res.append(n) # need to append because we need to keep adding to the res until we meet the most "k"
                if len(res) == k:
                    return res

    # wrong answer: this is  for exactly k frequent elements
    '''
    def topKFrequent(self, nums, k):
        num_freq = {}
        output = []
        for num in nums:
            count = num_freq.get(num, k) - 1
            if count == 0:
                output.append(num)
            num_freq[num] = count
        return output
    '''