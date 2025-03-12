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
                    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                    for neighbor in neighbors:
                        if neighbor[0] in range(len(grid)) and neighbor[1] in range(len(grid[0])) and \
                                grid[neighbor[0]][neighbor[1]] == "1" and neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)

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
