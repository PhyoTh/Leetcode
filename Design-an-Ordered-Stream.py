1class OrderedStream:
2
3    def __init__(self, n: int):
4        self.list = [None] * n
5        self.returnPtr = -1
6
7    def insert(self, idKey: int, value: str) -> List[str]:
8        self.list[idKey - 1] = value
9
10        result = []
11        walker = self.returnPtr + 1
12
13        while walker < len(self.list):
14            if self.list[walker]:
15                result.append(self.list[walker])
16                self.returnPtr = walker
17            else:
18                break
19            walker += 1
20        return result
21
22# Your OrderedStream object will be instantiated and called as such:
23# obj = OrderedStream(n)
24# param_1 = obj.insert(idKey,value)