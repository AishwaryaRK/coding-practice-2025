from typing import List
from collections import deque


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    visited = set()
    queue = deque()
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                queue.append((i, j))
                while queue:
                    i, j = queue.popleft()
                    visited.add((i, j))
                    if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited:
                        queue.append((i - 1, j))
                        visited.add((i - 1, j))
                    if i + 1 < len(grid) and grid[i + 1][j] == "1" and (i + 1, j) not in visited:
                        queue.append((i + 1, j))
                        visited.add((i + 1, j))
                    if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited:
                        queue.append((i, j - 1))
                        visited.add((i, j - 1))
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and (i, j + 1) not in visited:
                        queue.append((i, j + 1))
                        visited.add((i, j + 1))
                num_islands += 1
    return num_islands


print(numIslands([["1", "1", "1", "1", "0"],
                  ["1", "1", "0", "1", "0"],
                  ["1", "1", "0", "0", "0"],
                  ["0", "0", "0", "0", "0"]]))

print(numIslands([["1", "1", "0", "0", "0"],
                  ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"],
                  ["0", "0", "0", "1", "1"]]))
