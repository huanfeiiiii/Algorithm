# _*_ coding:utf-8 _*_

l1 = [2, 8, 3]
l2 = [5, 6, 4]
k = 0
for i in range(len(l1)):
    if l1[i] + l2[i] >= 10:
        print((l1[i] + l2[i]) // 10)
