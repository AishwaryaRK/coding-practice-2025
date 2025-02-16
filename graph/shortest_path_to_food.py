import collections
from typing import List


def find_user_location(grid: List[List[str]]) -> (int, int):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '*':
                return r, c
    return -1, -1


def shortest_path(grid: List[List[str]]) -> int:
    user_r, user_c = find_user_location(grid)

    queue = collections.deque([(user_r, user_c)])
    visited = set()

    def bfs(path, queue) -> int:
        rows = len(grid)
        cols = len(grid[0])
        new_queue = collections.deque()
        while queue:
            r, c = queue.pop()
            if grid[r][c] == '#':
                return path
            visited.add((r, c))
            next_cells = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for next_cell in next_cells:
                if next_cell[0] in range(rows) and next_cell[1] in range(cols) \
                        and next_cell not in visited and grid[next_cell[0]][next_cell[1]] != 'X':
                    new_queue.append(next_cell)
        if new_queue:
            return bfs(path + 1, new_queue)
        else:
            return -1

    return bfs(0, queue)


print(shortest_path([['X', 'X', 'X', 'X', 'X', 'X'],
                     ['X', '*', 'O', 'O', 'O', 'X'],
                     ['X', 'O', 'O', '#', 'O', 'X'],
                     ['X', 'X', 'X', 'X', 'X', 'X']]))

print(shortest_path(
    [['X', 'X', 'X', 'X', 'X'],
     ['X', '*', 'X', 'O', 'X'],
     ['X', 'O', 'X', '#', 'X'],
     ['X', 'X', 'X', 'X', 'X']]
))

print(shortest_path([
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '*', 'O', 'X', 'O', '#', 'O', 'X'],
    ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'O', 'O', '#', 'O', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]))

print(shortest_path([['O', '*'],
                     ['#', 'O']]))

print(shortest_path([['X', '*'],
                     ['#', 'X']]))
