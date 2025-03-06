import collections
from typing import List


def find_start(grid: List[str]) -> (int, int):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return (r, c)


def num_of_keys(grid: List[str]) -> int:
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c].islower():
                count += 1
    return count


def shortestPathAllKeys(grid: List[str]) -> int:
    start_r, start_c = find_start(grid)
    keys_count = num_of_keys(grid)
    print("* ",keys_count)
    queue = collections.deque([(start_r, start_c), (None, None)])
    visited = set()
    keys = set()
    steps = 0
    while queue:
        r, c = queue.popleft()
        if r == None and c == None:
            if queue:
                steps += 1
                queue.append((None, None))
            continue
        if (r, c) in visited:
            continue
        next_steps = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for next_step in next_steps:
            next_r = next_step[0]
            next_c = next_step[1]
            if next_r in range(len(grid)) and next_c in range(len(grid[0])) and grid[next_r][next_c] != "#" and (
                    next_r, next_c) not in visited:
                if grid[next_r][next_c].islower():
                    keys.add(grid[next_r][next_c])
                    queue.append((next_r, next_c))
                    keys_count -= 1
                    if keys_count == 0:
                        return steps + 1
                if grid[next_r][next_c].isupper() and grid[next_r][next_c].lower() in keys:
                    queue.append((next_r, next_c))
                if grid[next_r][next_c] == ".":
                    queue.append((next_r, next_c))
        visited.add((r, c))

    return -1


# print(shortestPathAllKeys(grid=["@.a..", "###.#", "b.A.B"]))
# print(shortestPathAllKeys(grid=["@..aA", "..B#.", "....b"]))
# print(shortestPathAllKeys(grid = ["@Aa"]))
print(shortestPathAllKeys(["@...a",".###A","b.BCc"]))