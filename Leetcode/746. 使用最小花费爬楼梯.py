# _*_ coding:utf-8 _*_

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
dp = []
for i in range(3, len(cost)):
    cost[i] = cost[i] + (min(cost[i-1], cost[i-2]))
print(cost)