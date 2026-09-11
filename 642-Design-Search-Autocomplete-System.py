class TrieNode:
    def __init__(self, c: str):
        self.c = c
        self.next = {}
        self.indicies = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.bank = list(zip(sentences, times))
        self.bank.sort(key=lambda x: (-x[1], x[0]))
        self.root = TrieNode("")
        self.walker = self.root

        for i in range(len(self.bank)):
            walker = self.root
            for c in self.bank[i][0]:
                if c not in walker.next:
                    walker.next[c] = TrieNode(c)
                walker = walker.next[c]
                walker.indicies.append(i)

    def input(self, c: str) -> List[str]:
        if c not in self.walker.next:
            return []
        elif c == '#':
            self.walker = self.root
            return []

        self.walker = self.walker.next[c]
        result = []
        for index in self.walker.indicies:
            result.append(self.bank[index][0])
            if len(result) == 3:
                break
        return result

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)