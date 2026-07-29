class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        n = len(digits)
        result = []

        def backtrack(digit_pos: int, word: list):
            if len(word) == n:
                result.append(''.join(word))
                return
            
            for i in range(len(num_dict[digits[digit_pos]])):
                word.append(num_dict[digits[digit_pos]][i])
                backtrack(digit_pos + 1, word)
                word.pop()
        
        backtrack(0, [])
        return result