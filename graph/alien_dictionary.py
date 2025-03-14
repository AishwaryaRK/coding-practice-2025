import collections
from typing import List


def find_alpha_order(words: List[str]) -> str:
    graph = collections.defaultdict(set)
    indegrees = collections.defaultdict(int)
    indegrees[words[0][0]] = 0
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        if word1[0] != word2[0]:
            graph[word1[0]].add(word2[0])
            indegrees[word2[0]] += 1
            continue
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                graph[w1].add(w2)
                indegrees[w2] += 1
                break
    print(graph)
    print(indegrees)

    order = ""
    sources = collections.deque([v for v, n in indegrees.items() if n == 0])
    while sources:
        s = sources.popleft()
        order += s
        for v in graph[s]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                sources.append(v)
    return order


print(find_alpha_order(words=["wrt", "wrf", "er", "ett", "rftt"]))
print(find_alpha_order(words = ["z","x"]))
print(find_alpha_order(words = ["z","x","z"]))