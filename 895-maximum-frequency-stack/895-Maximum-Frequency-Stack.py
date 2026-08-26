from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.freq = {} # (key=val : value=frequency)
        self.freq_list = defaultdict(list) # (key=frequency counter : value=stack)
        self.most_freq = 0

    def push(self, val: int) -> None:
        prev_freq = self.freq.get(val, 0)
        self.freq[val] = prev_freq + 1
        self.freq_list[prev_freq + 1].append(val)
        self.most_freq = max(self.most_freq, prev_freq + 1)

    def pop(self) -> int:
        if self.most_freq == 0:
            return -1
        
        val = self.freq_list[self.most_freq].pop()
        if len(self.freq_list[self.most_freq]) == 0:
            del self.freq_list[self.most_freq]
            self.most_freq -= 1
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()