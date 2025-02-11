from typing import List


class Solution:
    def __isValidRow(self, i, board):
        nums = [0] * 10
        for j in range(len(board)):
            n = board[i][j]
            if n != ".":
                n = int(n)
                nums[n] += 1
                if nums[n] > 1:
                    return False
        return True

    def __isValidCol(self, i, board):
        nums = [0] * 10
        for j in range(len(board)):
            n = board[j][i]
            if n != ".":
                n = int(n)
                nums[n] += 1
                if nums[n] > 1:
                    return False
        return True

    def __isValidUnitGrid(self, start_r, start_c, end_r, end_c, board):
        nums = [0] * 10
        for r in range(start_r, end_r):
            for c in range(start_c, end_c):
                n = board[r][c]
                if n != ".":
                    n = int(n)
                    nums[n] += 1
                    if nums[n] > 1:
                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.__isValidRow(i, board):
                return False
            if not self.__isValidCol(i, board):
                return False
        r = 0
        while r in range(0, len(board) - 2):
            c = 0
            while c in range(0, len(board) - 2):
                if not self.__isValidUnitGrid(r, c, r + 3, c + 3, board):
                    return False
                c += 3
            r += 3
        return True


# print(Solution().isValidSudoku(
#     [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#      [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#      ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#      [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

# print(Solution().isValidSudoku(
#
#     [[".", ".", ".", ".", ".", ".", "5", ".", "."],
#      [".", ".", ".", ".", ".", ".", ".", ".", "."],
#      [".", ".", ".", ".", ".", ".", ".", ".", "."],
#      ["9", "3", ".", ".", "2", ".", "4", ".", "."],
#      [".", ".", "7", ".", ".", ".", "3", ".", "."],
#      [".", ".", ".", ".", ".", ".", ".", ".", "."],
#      [".", ".", ".", "3", "4", ".", ".", ".", "."],
#      [".", ".", ".", ".", ".", "3", ".", ".", "."],
#      [".", ".", ".", ".", ".", "5", "2", ".", "."]]))

