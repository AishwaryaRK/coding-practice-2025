import collections
from typing import List


def evalRPN(tokens: List[str]) -> int:
    math_signs = set(["+", "-", "/", "*"])
    stack = collections.deque()
    for t in tokens:
        if t in math_signs:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack.pop()


print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
