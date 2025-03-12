from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    cache = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

    def build_cache(i, j):
        if i not in range(len(matrix)) or j not in range(len(matrix[0])):
            return 0
        if cache[i][j] != -1:
            return cache[i][j]
        n1 = build_cache(i + 1, j)
        n2 = build_cache(i, j + 1)
        n3 = build_cache(i + 1, j + 1)
        n = min(n1, n2, n3)
        sq = 0 if matrix[i][j] == "0" else 1 + n
        cache[i][j] = sq
        return cache[i][j]

    build_cache(0, 0)
    print(cache)

    max_sq = max(max(row) for row in cache)
    return max_sq * max_sq


print(maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))

print(maximalSquare([["0"]]))
