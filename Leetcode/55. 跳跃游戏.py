# _*_ coding:utf-8 _*_

nums = [2, 4, 4, 2, 0, 3, 1, 4, 1, 3, 2, 0, 1, 1, 2, 1, 0, 1, 4]

max_n = nums[0]

for i, num in enumerate(nums):
    if i <= max_n:
        max_n = max(num + i, max_n)
    else:
        print(i)
