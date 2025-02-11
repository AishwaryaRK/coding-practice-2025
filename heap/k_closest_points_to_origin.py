import heapq
import math
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    points_dist = [[math.sqrt(x * x + y * y), x, y] for x, y in points]
    heapq.heapify(points_dist)
    result = []
    for i in range(k):
        p = heapq.heappop(points_dist)
        result.append([p[1], p[2]])
    return result


print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
