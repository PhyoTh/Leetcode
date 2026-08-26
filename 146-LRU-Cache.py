'''
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

capacity = 2
{
3
1
}

[]
'''
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.nodes = {}
        self.head = Node(-1, -1)
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        cur_node = self.nodes[key]
        if cur_node != self.tail:
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
            
            self.tail.next = cur_node
            cur_node.prev = self.tail
            cur_node.next = None
            self.tail = cur_node
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            if key not in self.nodes:
                print("Sequence reference for this {key} not found...")
                return
            cur_node = self.nodes[key]
            if cur_node != self.tail:
                cur_node.prev.next = cur_node.next
                cur_node.next.prev = cur_node.prev
                
                self.tail.next = cur_node
                cur_node.prev = self.tail
                cur_node.next = None
                self.tail = cur_node
        else:
            if len(self.nodes) == self.capacity:
                remove_node = self.head.next
                self.head.next = remove_node.next
                if remove_node.next:
                    remove_node.next.prev = self.head
                if self.tail == remove_node:
                    self.tail = None

                del self.nodes[remove_node.key]
                del self.dict[remove_node.key]
                del remove_node
            
            node = Node(key, value)
            if self.tail == None:
                self.head.next = node
                node.prev = self.head
            else:
                self.tail.next = node
                node.prev = self.tail
            
            self.tail = node
            self.nodes[key] = node
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)