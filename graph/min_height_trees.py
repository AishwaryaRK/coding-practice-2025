import collections
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if not edges:
        return [0]
    degrees = collections.defaultdict(int)
    adajacency_list = collections.defaultdict(list)
    for edge in edges:
        u = edge[0]
        v = edge[1]
        degrees[u] += 1
        degrees[v] += 1
        adajacency_list[u].append(v)
        adajacency_list[v].append(u)

    while len(degrees) > 2:
        for node in list(degrees.keys()):
            degree = degrees[node]
            if degree == 1:
                # degrees.pop(node)
                del degrees[node]
                for neighbor in adajacency_list[node]:
                    degrees[neighbor] -= 1

    return list(degrees.keys())


print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(findMinHeightTrees(1, []))
