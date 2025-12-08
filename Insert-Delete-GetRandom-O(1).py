1class RandomizedSet:
2    import random
3    def __init__(self):
4        self.element = []
5        self.hash = {}
6
7    def insert(self, val: int) -> bool:
8        if val in self.hash:
9            return False
10        self.element.append(val)
11        self.hash[val] = len(self.element) - 1
12        return True        
13
14    def remove(self, val: int) -> bool:
15        if val not in self.hash:
16            return False
17        here = self.hash[val]
18        self.hash[self.element[-1]] = here
19        
20        swap = self.element[here]
21        self.element[here] = self.element[-1]
22        self.element[-1] = swap
23        
24        self.element.pop()
25        del self.hash[val]
26
27        return True
28
29    def getRandom(self) -> int:
30        return random.choice(self.element)
31
32
33# Your RandomizedSet object will be instantiated and called as such:
34# obj = RandomizedSet()
35# param_1 = obj.insert(val)
36# param_2 = obj.remove(val)
37# param_3 = obj.getRandom()