# _*_ coding:utf-8 _*_

s = "??"
s = list(s)
left = 1
if len(s) == 1:
    s[0] = 'a'
while left < len(s)-1:
    if s[left] == '?':
        num = 97
        while chr(num) in (s[left-1] + s[left+1]):
            num += 1
        s[left] = chr(num)
    left += 1
if s[0] == '?':
    num = 97
    while chr(num) == s[1]:
        num += 1
    s[0] = chr(num)
if s[-1] == '?':
    num = 97
    while chr(num) == s[-2]:
        num += 1
    s[-1] = chr(num)
print(s)