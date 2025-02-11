from typing import List

map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 1:
        return map[digits[0]]
    result = []
    combinations = letterCombinations(digits[1:])
    for alpha in map[digits[0]]:
        for c in combinations:
            result.append(alpha + c)
    return result


print(letterCombinations("234"))
