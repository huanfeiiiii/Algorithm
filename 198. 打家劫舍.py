# _*_ coding:utf-8 _*_

nums = [1, 2, 3, 1]
dp = [nums[0], max(nums[:2])]
for i in range(2, len(nums)):
    dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
print(dp)
