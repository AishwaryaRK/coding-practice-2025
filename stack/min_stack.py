import collections


class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.min_stack = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        top_min = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(top_min, val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        a = self.stack[-1]
        return a

    def getMin(self) -> int:
        a = self.min_stack[-1]
        return a


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
