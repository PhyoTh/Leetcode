import bisect
class TrieNode:
    def __init__(self, c: str):
        self.c = c
        self.next = {}
        self.sentences = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        bank = list(zip(sentences, times))
        bank.sort(key=lambda x: (-x[1], x[0]))
        self.freq = {}
        self.root = TrieNode("")

        for i in range(len(bank)):
            walker = self.root
            for c in bank[i][0]:
                if c not in walker.next:
                    walker.next[c] = TrieNode(c)
                walker = walker.next[c]
                walker.sentences.append(bank[i][0])
            
            self.freq[bank[i][0]] = bank[i][1]
        
        self.walker = self.root
        self.inputStr = []
    
    def update(self) -> None:
        searchStr = ''.join(self.inputStr)
        self.freq[searchStr] = self.freq.get(searchStr, 0) + 1

        walker = self.root
        for c in self.inputStr:
            if c not in walker.next:
                walker.next[c] = TrieNode(c)
            walker = walker.next[c]
            if searchStr not in walker.sentences:
                walker.sentences.append(searchStr)
            walker.sentences.sort(key=lambda x:(-(self.freq[x]), x))
        
        self.inputStr = []
        self.walker = self.root

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.update()
            return []
        
        self.inputStr.append(c)

        if self.walker is None or c not in self.walker.next:
            self.walker = None
            return []
        
        self.walker = self.walker.next[c]
        return self.walker.sentences[:min(3, len(self.walker.sentences))]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)