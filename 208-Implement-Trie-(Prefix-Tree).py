class Node:
    def __init__(self, char = ''):
        self.char = char
        self.end = False
        self.next = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        walker = self.root

        for char in word:
            if char not in walker.next:
                walker.next[char] = Node(char)
            walker = walker.next[char]

        walker.end = True

    def search(self, word: str) -> bool:
        walker = self.root

        for char in word:
            if char not in walker.next:
                return False
            walker = walker.next[char]
        
        return walker.end

    def startsWith(self, prefix: str) -> bool:
        walker = self.root

        for char in prefix:
            if char not in walker.next:
                return False
            walker = walker.next[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)