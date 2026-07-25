class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(valid_paren: list, open_count: int, close_count: int):
            if len(valid_paren) == n * 2:
                if open_count == n and close_count == n:
                    result.append(''.join(valid_paren))
                return
            
            for paren in ['(', ')']:
                if paren == '(' and open_count < n:
                    valid_paren.append(paren)
                    backtrack(valid_paren, open_count + 1, close_count)
                    valid_paren.pop()
                elif paren == ')' and open_count > close_count:
                    valid_paren.append(paren)
                    backtrack(valid_paren, open_count, close_count + 1)
                    valid_paren.pop()

        backtrack([], 0, 0)
        return result