class charNode:
    def __init__(self, char, last=False):
        self.char = char
        self.last = last
        self.child = {} # {key (char) : charNode}

class WordDictionary:
    def __init__(self):
        self.root = charNode("")

    def addWord(self, word: str) -> None:
        walker = self.root
        for char in word:
            if char not in walker.child:             
                walker.child[char] = charNode(char)

            walker = walker.child[char]
        walker.last = True

    def search(self, word: str) -> bool:
        def search_in_node(i, node):
            if i == len(word): # last char
                return node.last

            char = word[i]
            if char == '.':
                # check all the child in next level
                if len(node.child) == 0:
                    return False
                for child_node in node.child.values():
                    if search_in_node(i + 1, child_node):
                        return True
                return False

            else:
                if char not in node.child:
                    return False
                return search_in_node(i + 1, node.child[char])
    
        return search_in_node(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)