# _*_ coding:utf-8 _*_

import math

l1 = []
for _ in range(int(input())):
    max_num = 0
    num = 0
    m, n = map(int, input().split(' '))
    for i in range(min(m, n)):
        if math.gcd(m + i, n + i) > max_num:
            max_num = math.gcd(m + i, n + i)
            num = i
    l1.append(num)
for i in l1:
    print(i)
