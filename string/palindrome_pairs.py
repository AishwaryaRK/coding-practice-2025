from typing import List


def is_palindrome(word):
    start = 0
    end = len(word) - 1
    while start <= end:
        if word[end] != word[start]:
            return False
        start += 1
        end -= 1
    return True


def palindromePairs(words: List[str]) -> List[List[int]]:
    word_map = {word: i for i, word in enumerate(words)}
    pairs = []
    for i, word in enumerate(words):
        if "" in word_map and i != word_map[""] and is_palindrome(word):
            pairs.append([i, word_map[""]])
            pairs.append([word_map[""], i])
        r = word[::-1]
        if r in word_map and i != word_map[r]:
            pairs.append([i, word_map[r]])
        start = 0
        end = len(word) - 1
        while end > start:
            while word[end] != word[start]:
                end -= 1
            prefix = word[start:end + 1]
            suffix = word[end + 1:]
            reverse_suffix = suffix[::-1]
            if is_palindrome(prefix) and reverse_suffix in word_map and i != word_map[reverse_suffix]:
                pairs.append([word_map[reverse_suffix], i])
            end -= 1
    return pairs


print(palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(palindromePairs(["bat", "tab", "cat"]))
print(palindromePairs(["a", ""]))
