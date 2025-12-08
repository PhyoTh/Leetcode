1class MagicDictionary:
2
3    def __init__(self):
4        from collections import defaultdict
5        self.dictionary = defaultdict(list)
6
7    def buildDict(self, dictionary: List[str]) -> None:
8        for word in dictionary:
9            self.dictionary[len(word)].append(word)
10
11    def search(self, searchWord: str) -> bool:
12        return any(sum(a!=b for a, b in zip(searchWord, candidate)) == 1 for candidate in self.dictionary[len(searchWord)])
13
14
15# Your MagicDictionary object will be instantiated and called as such:
16# obj = MagicDictionary()
17# obj.buildDict(dictionary)
18# param_2 = obj.search(searchWord)