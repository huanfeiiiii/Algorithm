# _*_ coding:utf-8 _*_

rowIndex = 4
dp = [1 for _ in range(rowIndex + 1)]

for i in range(rowIndex):
    for j in range(i, 0, -1):
        dp[j] = dp[j] + dp[j-1]
print(dp)
