# _*_ coding:utf-8 _*_

nums = [2, 3, 1, 1, 4]

point = 0
k = 0
while point != len(nums) - 1:
    d1 = {}
    for i, j in enumerate(nums[point:nums[point] + point + 1]):
        d1[i + point] = i + point + j
    if len(nums) - 1 in d1:
        k += 1
        break
    jump = sorted(d1.items(), key=lambda x: x[1])[-1][0]
    point = jump
    k += 1
print(k)
