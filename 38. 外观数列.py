# _*_ coding:utf-8 _*_
import time

s = '1'
for i in range(30):
    temp = s[0]
    l1 = []
    for i in s[1:]:
        if temp[-1] != i:
            l1.append(str(len(temp))+str(temp[0]))
            temp = ''
        temp += i
    l1.append(str(len(temp))+str(temp[0]))
    s = ''.join(l1)
print(s)
