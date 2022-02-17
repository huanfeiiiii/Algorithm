# -*- coding:utf-8 -*-

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

for i in range(1, len(nums)):
    nums[i] += max(nums[i-1], 0)
print(max(nums))
