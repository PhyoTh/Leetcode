class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = None
        self.map = {}
    
    def length(self) -> int:
        return len(self.map)
    
    def push(self, key: int) -> None:
        node = Node(key)
        
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        if nxt:
            nxt.prev = node
        else:
            self.tail = node
        self.map[key] = node

    def pop(self) -> int:
        if len(self.map) == 0:
            return -1
        
        self.tail.prev.next = None
        key = self.tail.key
        self.tail = self.tail.prev if self.tail.prev != self.head else None

        del self.map[key]
        return key

    def remove(self, key: int) -> None:
        if len(self.map) == 0 or key not in self.map:
            return -1
        
        node = self.map[key]
        nxt = node.next
        node.prev.next = nxt
        if nxt:
            nxt.prev = node.prev
        else:
            self.tail = node.prev if node.prev is not self.head else None
        del self.map[key]

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {} # key: key, value: (value, freq)
        self.freq_list = defaultdict(LinkedList) # key: freq, value: LinkedList
        self.lf = 0

    def counter(self, key: int, value: Optional[int] = -1) -> None:
        val, count = self.dict[key]
        val = value if value != -1 else val
        self.dict[key] = (val, count + 1)
        self.freq_list[count].remove(key)
        self.freq_list[count + 1].push(key)

        if self.freq_list[count].length() == 0:
            del self.freq_list[count]
            if count == self.lf:
                self.lf = count + 1
    
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        self.counter(key)
        return self.dict[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.dict:
            self.counter(key, value)
            return

        if self.capacity == len(self.dict) and key not in self.dict:
            evicted = self.freq_list[self.lf].pop()
            if self.freq_list[self.lf].length() == 0:
                del self.freq_list[self.lf]
            del self.dict[evicted]

        self.dict[key] = (value, 1)
        self.freq_list[1].push(key)
        self.lf = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)