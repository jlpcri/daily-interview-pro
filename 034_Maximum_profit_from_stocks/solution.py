def buy_and_sell(arr):
    # profit holds the difference between 'current price'
    # and the 'minimum of prior prices'
    profit = [0]
    for i in range(1, len(arr)):
        # print(i, ': ', arr[i], ': ', arr[:i])
        profit.append(arr[i] - min(arr[:i]))

    print(profit)
    # return the maximum of profit
    return max(profit)


arr = [9, 11, 8, 5, 7, 10]
print(buy_and_sell(arr=arr))
# 10 - 5 = 5

print(buy_and_sell([7, 1, 5, 3, 6, 4]))
# 6 - 1 = 5