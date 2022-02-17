# -*- coding:utf-8 -*-

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

# 第二种

nums = [1, 1, 2]

nums_list = [[[], nums]]

while len(nums_list[0][1]) > 0:
    stack = nums_list.pop(0)
    for i in stack[1]:
        right = stack[1][:]
        right.remove(i)
        left = stack[0][:]
        left.append(i)
        nums_list.append([left, right])

print([i[0] for i in nums_list])
