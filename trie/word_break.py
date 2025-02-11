import collections
from typing import List


class Trie:

    def __init__(self):
        self.dict = collections.defaultdict(dict)

    def insert(self, word: str) -> None:
        t = self.dict
        for i, w in enumerate(word):
            if w not in t:
                t[w] = {}
            t = t[w]
            if i == len(word) - 1:
                t[None] = True

    def search(self, word: str) -> bool:
        t = self.dict
        for i, w in enumerate(word):
            if w not in t:
                return False
            t = t[w]
            if i == len(word) - 1:
                return None in t
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.dict
        for i, w in enumerate(prefix):
            if w not in t:
                return False
            t = t[w]
        return True


def wordBreak(s: str, wordDict: List[str]) -> bool:
    trie = Trie()
    for word in wordDict:
        trie.insert(word)

    print(trie.dict)
    def dp(s: str) -> bool:
        if s == "":
            return True
        i = 0
        j = 1
        while j <= len(s):
            if trie.search(s[i:j]):
                if dp(s[j:]):
                    return True
            j += 1
        return False

    return dp(s)


# print(wordBreak("applepenapple", ["apple", "pen"]))
# print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(wordBreak("aaaaaaa", ["aaaa", "aaa"]))
