# -*- coding:utf-8 -*-
# DFS + 历史检索

nums = [1, 1, 2]

nums_list = [[[], nums]]
history = []
while len(nums_list[0][1]) > 0:
    stack = nums_list.pop(0)
    if stack in history:
        continue
    history.append(stack)
    for i in stack[1]:
        right = stack[1][:]
        right.remove(i)
        left = stack[0][:]
        left.append(i)
        nums_list.append([left, right])

print([i[0] for i in nums_list])
