class Node:
    
    def __init__(self, char: str, last: bool, nxt: dict):
        self.char = char
        self.last = last
        self.nxt = nxt

class Trie:

    def __init__(self):
        self.root = Node("", False, {})

    def insert(self, word: str) -> None:
        walker = self.root
        for char in word:
            if char not in walker.nxt:
                insert_node = Node(char, False, {})
                walker.nxt[char] = insert_node

            walker = walker.nxt[char]
        walker.last = True

    def search(self, word: str) -> bool:
        walker = self.root
        for char in word:
            if char not in walker.nxt:
                return False
            walker = walker.nxt[char]

        return walker.last

    def startsWith(self, prefix: str) -> bool:
        walker = self.root
        for char in prefix:
            if char not in walker.nxt:
                return False
            walker = walker.nxt[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)