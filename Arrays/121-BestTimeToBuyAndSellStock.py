def first(prices):
    buy = prices.index(min(prices))

    if prices.index(min(prices)) == len(prices) - 1:
        print(0)
    else:
        sell = max(prices[buy:]) - min(prices)
        print(sell)


def second(prices):
    buy = prices.index(min(prices))

    if len(prices) == 1:
        print(0)

    elif len(prices) == 2:
        if prices[0] > prices[1]:
            print(0)

    elif prices.index(min(prices)) == len(prices) - 1:
        for i in range(len(prices) - 2):
            if prices[i] < prices[i + 1]:
                small = prices[i]
            else:
                small = prices[i + 1]
        sell = max(prices[prices.index(small):]) - small
        print(sell)

    else:
        sell = max(prices[buy:]) - min(prices)
        print(sell)


def third(prices):
    small = []
    cont = 1
    sell = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            small.append(prices[i])
        else:
            cont += 1

    if cont == len(prices):
        print(0)

    else:
        for i in range(len(small)):
            if (max(prices[prices.index(small[i]):]) - small[i]) > sell:
                sell = max(prices[prices.index(small[i]):]) - small[i]
        print(sell)


prices = [7,1,5,3,6,4]
third(prices)