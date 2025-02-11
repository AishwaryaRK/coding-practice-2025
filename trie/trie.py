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

    def all_words_with_prefix(self, prefix: str) -> List[str]:
        def traverse(t):
            words = []
            for w, next_t in t.items():
                if w == None:
                    words.append("")
                else:
                    suffixes = traverse(next_t)
                    for suffix in suffixes:
                        words.append(w + suffix)
            return words

        t = self.dict
        for i, w in enumerate(prefix):
            if w not in t:
                return []
            t = t[w]

        suffixes = traverse(t)
        words = []
        for suffix in suffixes:
            words.append(prefix + suffix)

        return words


t = Trie()
t.insert("apple")
t.insert("app")
t.insert("ape")
t.insert("alex")
t.insert("elephant")
t.insert("element")
t.insert("elemental")
print(t.all_words_with_prefix("ele"))
# print(t.search("apple"))
# print(t.search("app"))
