from typing import List
from collections import deque


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    vertex_indegree = {n: 0 for n in range(numCourses)}
    adjacency_list = {}
    for [u, v] in prerequisites:
        vertex_indegree[v] += 1
        if u in adjacency_list:
            adjacency_list[u].append(v)
        else:
            adjacency_list[u] = [v]
    sources = deque([v for v, d in vertex_indegree.items() if d == 0])
    topological_order = []
    while sources:
        s = sources.popleft()
        topological_order.append(s)
        if s in adjacency_list:
            for v in adjacency_list[s]:
                if v not in topological_order:
                    vertex_indegree[v] -= 1
                    if vertex_indegree[v] == 0:
                        sources.append(v)

    return len(topological_order) == numCourses


print(canFinish(2, [[1, 0]]))
