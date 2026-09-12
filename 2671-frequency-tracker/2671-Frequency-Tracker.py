from collections import defaultdict
class FrequencyTracker:
    def __init__(self):
        self.num2freq = defaultdict(int)
        self.freq2num = defaultdict(set)

    def add(self, number: int) -> None:
        if number in self.num2freq:
            self.freq2num[self.num2freq[number]].remove(number)
            if len(self.freq2num[self.num2freq[number]]) == 0:
                del self.freq2num[self.num2freq[number]]
        
        self.num2freq[number] += 1
        self.freq2num[self.num2freq[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if number not in self.num2freq:
            return

        self.freq2num[self.num2freq[number]].remove(number)
        if len(self.freq2num[self.num2freq[number]]) == 0:
            del self.freq2num[self.num2freq[number]]
        
        self.num2freq[number] -= 1
        if self.num2freq[number] == 0:
            del self.num2freq[number]
            return
        
        self.freq2num[self.num2freq[number]].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq2num


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)