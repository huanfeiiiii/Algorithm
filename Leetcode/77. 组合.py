# -*- coding:utf-8 -*-

n = 4
k = 2
l1 = [[i] for i in range(1, n + 1)]
while len(l1[0]) < k:
    temp = l1.pop(0)
    for i in range(temp[-1] + 1, n + 1):
        l2 = temp[:]
        l2.append(i)
        l1.append(l2)
print(l1)
