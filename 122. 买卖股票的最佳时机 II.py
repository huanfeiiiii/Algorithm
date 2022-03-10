# _*_ coding:utf-8 _*_

prices = [1, 2, 3, 4, 5]
k = 0
for i in range(len(prices) - 1):
    if prices[i] < prices[i + 1]:
        k += prices[i + 1] - prices[i]
print(k)
