def maxProfit(prices):
    if len(prices) < 2:
        return 0
    max_profit = 0
    buy_ptr = 0
    sell_ptr = 1
    while sell_ptr < len(prices):
        profit = prices[sell_ptr] - prices[buy_ptr]
        if profit > max_profit:
            max_profit = profit
        elif profit < 0:
            buy_ptr = sell_ptr
        sell_ptr += 1
    return max_profit