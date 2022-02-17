# -*- coding:utf-8 -*-

n = 59049
k = 0
num = 0
while num <= n:
    num = 3 ** k
    if num == n:
        print(True)
    k += 1
print(False)