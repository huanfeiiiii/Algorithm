# _*_ coding:utf-8 _*_

s = "10011111110010111011"

dp = [[s[0].count("1"), s[0].count("0")]]

for i in range(1, len(s)):
    temp = dp[-1][:]
    if s[i] == '0':
        temp[1] += 1
    else:
        temp[0] += 1
    dp.append(temp)
print(dp)