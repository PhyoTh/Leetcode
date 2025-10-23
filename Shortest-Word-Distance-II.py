from collections import defaultdict
class WordDistance:
    def __init__(self, wordsDict: List[str]):

        def construct_dict():
            result = defaultdict(list)
            for index, word in enumerate(wordsDict):
                result[word].append(index)
            return result

        self.word_dict = construct_dict()

    def shortest(self, word1: str, word2: str) -> int:
        shortest_dist = float('inf')
        word1_indicies = self.word_dict[word1]
        word2_indicies = self.word_dict[word2]

        for word1_index in word1_indicies:
            for word2_index in word2_indicies:
                shortest_dist = min(shortest_dist, abs(word1_index - word2_index))

        return shortest_dist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)