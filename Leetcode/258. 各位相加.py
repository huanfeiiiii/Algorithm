# _*_ coding:utf-8 _*_

num = 0
while num >= 10:
    num = sum([int(i) for i in list(str(num))])
print(num)
