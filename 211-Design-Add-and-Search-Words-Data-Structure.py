class Node:
    def __init__(self, val = ''):
        self.val = val
        self.end = False
        self.next = {}

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        walker = self.root

        for char in word:
            if char not in walker.next:
                walker.next[char] = Node(char)
            walker = walker.next[char]
        
        walker.end = True

    '''
                root
              /   |   \
              b   d   m
              |   |   |
              a   a   a
              |   |   |
              d   d   d
    search('.ad')
    '''
    def search(self, word: str) -> bool:
        n = len(word)
        if n == 0:
            return True

        def dfs(i, node) -> bool:
            if i == n:
                return node.end
            elif not node.next:
                return False
            elif word[i] != '.' and word[i] not in node.next:
                return False
            elif word[i] == '.':
                for neighbor in node.next.values():
                    if dfs(i + 1, neighbor):
                        return True
                return False

            return dfs(i + 1, node.next[word[i]])
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)