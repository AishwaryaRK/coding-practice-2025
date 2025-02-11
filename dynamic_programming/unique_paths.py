def uniquePaths(m: int, n: int) -> int:
    memoization = {}

    def dp(m, n):
        if (m == 1 and n > 1) or (n == 1 and m > 0):
            return 1
        if m == n == 1:
            return 0
        if (m, n) in memoization:
            return memoization[(m, n)]
        c1 = dp(m - 1, n)
        c2 = dp(m, n - 1)
        memoization[(m, n)] = c1 + c2
        return c1 + c2

    return dp(m, n)


# print(uniquePaths(3, 2))
print(uniquePaths(3, 7))
