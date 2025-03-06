import collections
import heapq
from typing import List, Dict


def construct_dijkshtra_table(src, graph) -> Dict:
    table = collections.defaultdict(list)
    table[src] = [0, src]
    visited = set()
    heap = []
    heapq.heappush(heap, (0, src))

    while heap:
        dist_cost, u = heapq.heappop(heap)
        if u in visited:
            continue
        for v, cost in graph[u]:
            if v not in table:
                table[v] = [cost + dist_cost, u]
                heapq.heappush(heap, (cost + dist_cost, v))
            else:
                if cost + dist_cost < table[v][0]:
                    table[v] = [cost + dist_cost, u]
                    heapq.heappush(heap, (cost + dist_cost, v))
        visited.add(u)
    print(table)
    return table


def find_hops(dijkshtra_table, src, dst) -> int:
    if dst not in dijkshtra_table:
        return -1
    hops = 0
    v = dst
    while v != src:
        v = dijkshtra_table[v][1]
        hops += 1
    return hops


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for edge in flights:
        u = edge[0]
        v = edge[1]
        cost = edge[2]
        graph[u].append([v, cost])

    dijkshtra_table = construct_dijkshtra_table(src, graph)

    hops = find_hops(dijkshtra_table, src, dst)
    if hops <= k:
        return hops
    return -1


print(findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3,
                        k=1))
