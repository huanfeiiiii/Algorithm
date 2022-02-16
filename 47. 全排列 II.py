# -*- coding:utf-8 -*-
# 未解决

nums = [-1, 2, -1, 2, 1, -1, 2, 1]

data = [[i, ] for i in nums]

for i in range(len(nums) - 1):
    l1 = []
    for j in data:
        for k in nums:
            if nums.count(k) > j.count(k):
                s = list(j)
                s.append(k)
                l1.append(s)
    data = l1
print(data)
# for i in data:
#     while data.count(i) != 1:
#         data.remove(i)
# print(data)
