# _*_ coding:utf-8 _*_

s = "aa"
if len(set(s)) == 1:
    print(s)
long = ''
for i in range(len(s)-1):
    left, right, temp = i, i, i
    while s[temp] == s[i]:
        right = temp
        temp += 1
        if left == -1 or right >= len(s)-1:
            break
    while s[left] == s[right]:
        if len(s[left:right + 1]) > len(long):
            long = s[left:right + 1]
        left -= 1
        right += 1
        if left == -1 or right >= len(s):
            break
print(long)