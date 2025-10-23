from collections import deque
class MyStack:
    def __init__(self):
        self.myStack = deque()

    def push(self, x: int) -> None:
        self.myStack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.myStack.pop()

    def top(self) -> int:
        return self.myStack[-1]

    def empty(self) -> bool:
        return len(self.myStack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()