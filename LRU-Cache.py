class LRUCache(object):

    def __init__(self, capacity):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache_queue = OrderedDict()

    def get(self, key):  # O(1)
        if key in self.cache_queue.keys():
            self.cache_queue.move_to_end(key)
            return self.cache_queue[key]
        return -1

    def put(self, key, value):  # O(1)
        if key in self.cache_queue.keys():
            self.cache_queue.move_to_end(key)
        else:  # key not in cache_queue
            if len(self.cache_queue) == self.capacity:  # max out capacity
                self.cache_queue.popitem(last=False)  # pop the first element of OrderedDict
    
        self.cache_queue[key] = value # to the end of OrderedDict

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)