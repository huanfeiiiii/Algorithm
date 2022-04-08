# _*_ coding:utf-8 _*_

prices = [0,1]

if len(prices) == 1:
    print(0)
    exit()
min_prices = prices[0]
l1 = []
for i in range(1, len(prices)):
    min_prices = min(min_prices, prices[i])
    l1.append(prices[i]-min_prices)
print(l1)