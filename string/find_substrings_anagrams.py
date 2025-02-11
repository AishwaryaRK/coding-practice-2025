import collections
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    p_hash = collections.defaultdict(int)
    for c in p:
        p_hash[c] += 1

    result = []
    s_hash = collections.defaultdict(int)
    i = 0
    start = 0
    while i < len(s):
        while (i - start) != len(p):
            s_hash[s[i]] += 1
            i += 1
        if s_hash == p_hash:
            result.append(start)
        s_hash[s[start]] -= 1
        if s_hash[s[start]] == 0:
            s_hash.pop(s[start])
        start += 1

    return result


print(findAnagrams("baa", "aa"))
