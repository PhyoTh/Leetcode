class Solution(object):
    def isValid(self, s):
        # leetcode solution with mapping
        from collections import deque
        stack = deque()
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

        # my code: this is easy but have to be careful for the edge cases
    #     open_parens = set(['(', '{', '['])
    #     close_parens = set([')', '}', ']'])

    #     from collections import deque
    #     stack = deque()

    #     for char in s:
    #         if char in open_parens:
    #             stack.append(char)
    #         elif char in close_parens:
    #             if len(stack) != 0:
    #                 popped = stack.pop()
    #                 if not self.corresponding_paren(popped, char):
    #                     return False
    #             else: # for the case of not having the open paren
    #                 return False
        
    #     return False if len(stack) != 0 else True

    # def corresponding_paren(self, popped, char):
    #     if popped == '(' and char == ')':
    #         return True
    #     elif popped == '{' and char == '}':
    #         return True
    #     elif popped == '[' and char == ']':
    #         return True
    #     return False