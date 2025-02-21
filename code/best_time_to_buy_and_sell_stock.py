def max_profit(prices: list[int]) -> int:
    min_price = min(prices)
    id_min = prices.index(min_price)

    max_price = max(prices[id_min:])

    return max_price - min_price


print(max_profit([2, 4, 1]))  # 2
