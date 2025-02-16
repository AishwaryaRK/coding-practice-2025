import collections
from typing import List


def is_one_connected_component(n, graph) -> bool:
    visited = set()

    queue = collections.deque([0])
    while queue:
        u = queue.pop()
        if u not in visited:
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)
            visited.add(u)
    return len(visited) == n


def is_cycle_present(graph):
    visited = set()
    queue = collections.deque([0])
    visited.add(0)
    while queue:
        u = queue.pop()
        for v in graph[u]:
            if v in visited:
                return True
            queue.append(v)
            visited.add(v)
    return False


def is_valid_tree(n: int, edges: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    for edge in edges:
        u = edge[0]
        v = edge[1]
        graph[u].append(v)
    if not is_one_connected_component(n, graph):
        return False
    if is_cycle_present(graph):
        return False
    return True


print(is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
