# _*_ coding:utf-8 _*_


candidates = [2, 3, 5]
target = 8
ans = [[target, []]]

res = []

while ans:
    temp = ans.pop(0)
    if temp[0] == 0:
        if sorted(temp[1]) not in res:
            res.append(sorted(temp[1]))
        continue

    for i in candidates:
        if temp[0] - i < 0:
            continue
        l1 = temp[1][:]
        l1.append(i)
        ans.append([temp[0] - i, l1])

print(res)
