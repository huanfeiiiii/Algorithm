# _*_ coding:utf-8 _*_

nums = [0]

l1 = list(map(str, nums))

while True:
    k = False
    for i in range(len(l1) - 1):
        if int(l1[i] + l1[i + 1]) < int(l1[i + 1] + l1[i]):
            l1[i], l1[i + 1] = l1[i + 1], l1[i]
            k = True
    if not k:
        break
print(l1)
