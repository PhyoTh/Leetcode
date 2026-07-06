class Node:
    def __init__(self, val=-1, key=-1, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.dict = {}

    def insert(self, insert_this):
        prev_tail = self.tail.prev
        prev_tail.next = insert_this
        self.tail.prev = insert_this
        insert_this.next = self.tail
        insert_this.prev = prev_tail

    def remove(self, remove_this):
        prev = remove_this.prev
        prev.next = remove_this.next
        remove_this.next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.dict.keys():
            return -1

        here = self.dict[key]
        self.remove(here)
        self.insert(here)
        return here.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            here = self.dict[key]
            here.val = value
            self.remove(here)
            self.insert(here)
        else:
            if len(self.dict) == self.capacity:
                here = self.head.next
                self.remove(here)
                del self.dict[here.key]
            temp = Node(value, key)
            self.dict[key] = temp
            self.insert(temp)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)