from typing import List
import valid_sudoku
import copy


class UnitGrid:
    def __init__(self, start_r, start_c, end_r, end_c):
        self.start_r = start_r
        self.start_c = start_c
        self.end_r = end_r
        self.end_c = end_c


class Solution:
    def __is_valid_num(self, n: int, r, c, unit_grid: UnitGrid, board) -> bool:
        return True

    def __get_unit_grid(self, r, c):
        return

    def __is_sudoku_solved(self, board) -> bool:
        for r in range(len(board)):
            if "." in board[r]:
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(board) -> (bool, List[List[str]]):
            if self.__is_sudoku_solved(board):
                return (True, board)
            for r in range(len(board)):
                for c in range(len(board)):
                    if board[r][c] == ".":
                        for n in range(1, 10):
                            # unit_grid = self.__get_unit_grid(r, c)
                            # if self.__is_valid_num(n, r, c, unit_grid, board):
                            b = copy.deepcopy(board)
                            b[r][c] = str(n)
                            if valid_sudoku.Solution().isValidSudoku(b):
                                # b = copy.deepcopy(board)
                                # b[r][c] = n
                                (is_complete, complete_board) = backtrack(b)
                                if is_complete:
                                    return (True, complete_board)
                        return (False, None)
            return (False, None)

        (_, board) = backtrack(board)
        print(board)


# Solution().solveSudoku(
#     [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#      [".", "9", "8", ".", ".", ".", ".", "6", "."],
#      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#      [".", "6", ".", ".", ".", ".", "2", "8", "."],
#      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# )

Solution().solveSudoku([[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                      [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
                      [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
                      [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
                      [".", ".", ".", "2", "7", "5", "9", ".", "."]])
