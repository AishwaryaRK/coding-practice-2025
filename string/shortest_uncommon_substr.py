import collections
from typing import List


def shortestSubstrings(arr: List[str]) -> List[str]:
    substrs = collections.defaultdict(list)
    a_substrs = collections.defaultdict(list)
    for a in arr:
        for l in range(1, len(a) + 1):
            for i in range(0, len(a) - l + 1):
                s = a[i:i + l]
                substrs[s].append(a)
                a_substrs[a].append(s)
    result = []
    for a, v in a_substrs.items():
        ans = ""
        for s in v:
            if len(substrs[s]) == 1:
                ans = s
                break
        result.append(ans)
    return result


print(shortestSubstrings(["cab", "ad", "bad", "c"]))
print(shortestSubstrings(["abc","bcd","abcd"]))