class Solution(object):
    '''
            ""
           /   \
        "("      ")"
       /   \     /  \
    "(("  "()"  ")("  "))"
    '''
    def generateParenthesis(self, n):
        result = []
        
        def rollout(curr_string, open_paren_count, close_paren_count):
            if len(curr_string) == 2*n:
                result.append("".join(curr_string))
                return
            if open_paren_count < n:
                curr_string.append("(")
                rollout(curr_string, open_paren_count+1, close_paren_count)
                curr_string.pop()
            if open_paren_count > close_paren_count:
                curr_string.append(")")
                rollout(curr_string, open_paren_count, close_paren_count+1)
                curr_string.pop()
    
        rollout([], 0, 0)
        return result