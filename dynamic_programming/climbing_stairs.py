def climbStairs(n: int) -> int:
    memoization = {}

    def dp(n):
        if n == 0:
            return 1
        if n in memoization:
            return memoization[n]
        w1 = w2 = 0
        if n - 2 >= 0:
            w1 = dp(n - 2)
        if n - 1 >= 0:
            w2 = dp(n - 1)
        memoization[n] = w1 + w2
        return w1 + w2

    return dp(n)


print(climbStairs(3))
