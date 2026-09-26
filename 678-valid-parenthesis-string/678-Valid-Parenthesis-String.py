class Solution:
    def checkValidString(self, s: str) -> bool:
        paren_stack = [] # keeps indicies of open paren
        star_stack = [] # keeps indicies of star

        for i in range(len(s)):
            if s[i] == '(':
                paren_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else: # i feel like this might be wrong, cuz its heuristic
                if paren_stack:
                    paren_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while paren_stack:
            if not star_stack:
                return False
            
            if paren_stack[-1] < star_stack[-1]:
                paren_stack.pop()
                star_stack.pop()
            else:
                return False
        
        return True