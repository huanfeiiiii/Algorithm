# _*_ coding:utf-8 _*_

bits = [1, 0, 1, 0]
right = len(bits) - 2
k = 0
while right >= 0:
    if bits[right] == 0:
        break
    else:
        right -= 1
        k += 1
print(k % 2 == 0)
