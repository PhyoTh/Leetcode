class TrieNode():
    def __init__(self):
        self.list = [None] * 26
        self.isEnd = False
    
    def setEnd(self):
        self.isEnd = True

    def getEnd(self):
        return self.isEnd

    def getKey(self, key):
        return self.list[ord(key) - ord('a')]

    def linkNodes(self, key, node):
        self.list[ord(key) - ord('a')] = node

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        walker = self.root

        for ch in word:
            nxt = walker.getKey(ch)
            if nxt is None: # if there doesn't exist such key
                nxt = TrieNode()
                walker.linkNodes(ch, nxt)
            walker = nxt
        walker.setEnd()
        

    def search(self, word):
        walker = self.root

        for ch in word:
            nxt = walker.getKey(ch)
            if nxt is None:
                return False
            
            walker = nxt
        return walker.getEnd()


    def startsWith(self, prefix):
        walker = self.root

        for ch in prefix:
            nxt = walker.getKey(ch)
            if nxt is None:
                return False
        
            walker = nxt
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)