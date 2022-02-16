# -*- coding:utf-8 -*-
# 已解决

nums = [1, 2, 3]

data = [[i, ] for i in nums]

for i in range(len(nums) - 1):
    l1 = []
    for j in data:
        for k in nums:
            if k not in j:
                s = list(j)
                s.append(k)
                l1.append(s)
    data = l1

print(data)
