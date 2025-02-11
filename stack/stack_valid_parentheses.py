from collections import deque


def isValid(s):
    stack = deque()
    valid_brackets = {'(': ')', '{': '}', '[': ']'}
    for bracket in s:
        if bracket in valid_brackets:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            stack_top = stack.pop()
            if valid_brackets[stack_top] != bracket:
                return False
    if len(stack) != 0:
        return False
    return True
