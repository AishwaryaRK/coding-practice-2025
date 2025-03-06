# Given a board that is a kingdom. The board is represented as an array of strings.
# Each string contains a number of tiles separated by a space.
# Each tile consists of a letter, and there can be 0-9 crowns.
# Your task is to calculate the total score. The score calculation is done by using the following formula:
# (number of same tiles in an area * number of crowns in that area)
# A board can be of any size no greater than 5x5.


from typing import List


def calc_board_score(board: List[List[int]]) -> int:
    visited = set()

    def floodfill(count, crown_count, r, c, type) -> (int, int):
        crown_count += int(board[r][c][1])
        count += 1
        visited.add((r, c))
        neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for (neighbor_r, neighbor_c) in neighbors:
            if neighbor_r in range(len(board)) and neighbor_c in range(len(board[0])) \
                    and (neighbor_r, neighbor_c) not in visited and board[neighbor_r][neighbor_c][0] == type:
                count, crown_count = floodfill(count, crown_count, neighbor_r, neighbor_c, type)
        return count, crown_count

    score = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (r, c) not in visited:
                count, crown_count = floodfill(0, 0, r, c, board[r][c][0])
                score += count * crown_count
    return score


print(calc_board_score([["L0", "W1", "W1", "W0", "F2"],
                        ["W0", "W0", "T0", "T0", "T0"],
                        ["W0", "W1", "T0", "R2", "R1"],
                        ["L0", "K0", "L1", "L0", "L0"],
                        ["R0", "C2", "C0", "L1", "T0"]]))
