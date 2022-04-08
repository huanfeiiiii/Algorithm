# _*_ coding:utf-8 _*_

s = "aab"
l1 = list(s)
l3 = []
while len(l1[-1]) < len(s)-1:
    l2 = []
    for i in l1:
        for j in s:
            l2.append(i+j)
            if i+j not in l3 and i+j == (i+j)[::-1]:
                l3.append(i+j)
    l1 = list(set(l2))
    # print(l1)
print(l3)