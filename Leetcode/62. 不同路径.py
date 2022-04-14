# _*_ coding:utf-8 _*_

m = 3
n = 3

dp = [1 for i in range(n)]

for i in range(m-1):

    for j in range(1, n):

        dp[j] = dp[j] + dp[j-1]
print(dp[-1])