class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        O(nlogn) Sol 1: Sort nums and count
        O(nlogn) Sol 2: Get nums count and sort
        O(klogn) Sol: use Heap and pop
        '''
        count = {}
        for num in nums: # O(n)
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items(): # O(n)
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1): # O(n)
            while len(freq[i]) > 0 and k > 0:
                temp = freq[i].pop()
                result.append(temp)
                k -= 1
            
            if k == 0:
                break
        return result