# -*- coding:utf-8 -*-

a = "abc"
b = "cabcabca"

if list(set(a)) != list(set(b)) and a not in b:
    print(-1)
k = 1
while b not in a:
    a += a
    print(a)
    k += 1
print(k)
