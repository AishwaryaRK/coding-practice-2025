import collections
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    rotten_oranges = []
    fresh_oranges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh_oranges += 1
            elif grid[i][j] == 2:
                rotten_oranges.append((i, j))
    queue = collections.deque()
    time = 0
    while rotten_oranges and fresh_oranges > 0:
        for n in range(len(rotten_oranges)):
            i, j = rotten_oranges.pop()
            if i - 1 in range(len(grid)) and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                queue.append((i - 1, j))
                fresh_oranges -= 1
            if i + 1 in range(len(grid)) and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                queue.append((i + 1, j))
                fresh_oranges -= 1
            if j - 1 in range(len(grid[0])) and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                queue.append((i, j - 1))
                fresh_oranges -= 1
            if j + 1 in range(len(grid[0])) and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                queue.append((i, j + 1))
                fresh_oranges -= 1
        time += 1
        rotten_oranges = queue

    if fresh_oranges == 0:
        return time

    return -1


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(orangesRotting([[0, 2]]))
