# -*- coding:utf-8 -*-

nums = [5, 4, -1, 7, 8]

for i in range(1, len(nums)):
    if nums[i - 1] > 0:
        nums[i] = nums[i - 1] + nums[i]

print(nums)
