import operator

operator_mapping = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in operator_mapping:
                val1 = stack.pop()
                val2 = stack.pop()
                result = operator_mapping[token](val2, val1)
                stack.append(int(result))
            else:
                stack.append(int(token))
        
        return stack[0]