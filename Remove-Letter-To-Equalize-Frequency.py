1class Solution:
2    def equalFrequency(self, word: str) -> bool:
3        from collections import Counter
4        word_dict = Counter(word)
5
6        for key, value in sorted(word_dict.items()):
7            word_dict[key] -= 1
8
9            if word_dict[key] == 0:
10                del word_dict[key]
11            if len(set(word_dict.values())) == 1:
12                return True
13            
14            word_dict[key] = word_dict.get(key, 0) + 1
15        return False