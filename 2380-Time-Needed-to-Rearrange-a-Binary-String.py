class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ''' O(n^2) '''
        # count = 0

        # while "01" in s:
        #     s = s.replace("01", "10")
        #     count += 1
        # return count

        ''' O(n) '''
        zeros = 0
        seconds = 0

        for char in s:
            if char == "0":
                zeros += 1
            else:
                if zeros > 0:
                    seconds = max(zeros, seconds + 1)
        
        return seconds