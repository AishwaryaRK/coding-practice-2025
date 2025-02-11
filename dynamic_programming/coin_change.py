from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    memoization = {}

    def dp(coins, amount):
        if amount == 0:
            return 0
        if amount in memoization:
            return memoization[amount]

        min_coins = -1
        for coin in coins:
            if coin <= amount:
                c = 1 + dp(coins, amount - coin)
                if c > 0:
                    min_coins = min(min_coins, c) if min_coins != -1 else c

        memoization[amount] = min_coins
        return min_coins

    return dp(coins, amount)


print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))

