# _*_ coding:utf-8 _*_

obstacleGrid = [[0,0],[1,0]]


dp = [0 for _ in range(len(obstacleGrid[0]))]
dp[0] = 1
for i in range(len(obstacleGrid)):
    if obstacleGrid[i][0] == 1:
        dp[0] = 0
    for j in range(1, len(obstacleGrid[0])):
        if obstacleGrid[i][j] == 1:
            dp[j] = 0
        else:
            dp[j] = dp[j] + dp[j - 1]
print(dp)
