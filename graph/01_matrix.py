import math


def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] != 0:
                if r == c == 0:
                    mat[r][c] = math.inf
                elif r - 1 >= 0 and c - 1 >= 0:
                    mat[r][c] = min(mat[r - 1][c], mat[r][c - 1]) + 1
                elif r - 1 >= 0:
                    mat[r][c] = mat[r - 1][c] + 1
                elif c - 1 >= 0:
                    mat[r][c] = mat[r][c - 1] + 1
    for r in range(len(mat) - 1, -1, -1):
        for c in range(len(mat[0]) - 1, -1, -1):
            if mat[r][c] != 0:
                if r + 1 < len(mat) and c + 1 < len(mat[0]):
                    mat[r][c] = min((min(mat[r + 1][c], mat[r][c + 1]) + 1), mat[r][c])
                elif r + 1 < len(mat):
                    mat[r][c] = min((mat[r + 1][c] + 1), mat[r][c])
                elif c + 1 < len(mat[0]):
                    mat[r][c] = min((mat[r][c + 1] + 1), mat[r][c])
    return mat


print(updateMatrix([[1, 0, 0], [0, 1, 0], [1, 1, 1]]))
