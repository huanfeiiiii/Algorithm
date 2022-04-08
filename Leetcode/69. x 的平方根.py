# _*_ coding:utf-8 _*_

x = 1

point = x // 2
left = 0
right = x

while right - left > 1:
    num = (right + left) // 2
    if num * num > x:
        right = num
    else:
        left = num
print(left)