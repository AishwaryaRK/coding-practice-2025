from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    if word == "":
        return True

    visited = set()

    def dfs(i, j, w):
        if w == len(word):
            return True
        if (i, j) in visited:
            return False
        if i not in range(len(board)) or j not in range(len(board[0])):
            return False
        if board[i][j] == word[w]:
            visited.add((i, j))
            w += 1
            if any([dfs(i + 1, j, w), dfs(i - 1, j, w), dfs(i, j + 1, w), dfs(i, j - 1, w)]):
                return True
            visited.remove((i,j))
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True
                visited = set()

    return False


# print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
# print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))

print(exist([["A", "B", "C", "E"],
             ["S", "F", "E", "S"],
             ["A", "D", "E", "E"]]
            , "ABCESEEEFS"))
