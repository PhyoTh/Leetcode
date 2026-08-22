from collections import defaultdict, deque
class Solution:
    def generate_wild(self, word: str) -> List(str):
        return [word[0: i] + '*' + word[i + 1:] for i in range(len(word))]
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wild_cards = defaultdict(list)
        adj_list = defaultdict(list)

        for i in range(-1, len(wordList)):
            if i == -1:
                word = beginWord
            else:
                word = wordList[i]
            
            for wild in self.generate_wild(word):
                if wild in wild_cards:
                    for other_word in wild_cards[wild]:
                        adj_list[word].append(other_word)
                        adj_list[other_word].append(word)
                wild_cards[wild].append(word)
            
        que = deque([beginWord])
        seen = set()
        level = -1

        while que:
            level += 1
            for _ in range(len(que)):
                word = que.popleft()

                if word == endWord:
                    return level + 1
                seen.add(word)

                for neighbor in adj_list[word]:
                    if neighbor in seen:
                        continue
                    que.append(neighbor)

        return 0
