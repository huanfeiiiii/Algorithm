# _*_ coding:utf-8 _*_
import itertools

l1 = []
for i in range(10):
    if i == 1:
        continue
    l1.append('111' + str(i))
for i in range(2):
    l1.append('222' + str(i))
num = 0
for i in l1:
    month = 0
    year = 0
    for j in list(set(itertools.permutations(i))):
        if 0 < int(''.join(j[:2])) <= 12:
            month += 1
    for j in list(set(itertools.permutations(i))):
        if 0 < int(''.join(j[:2])) <= 24 and 0 < int(''.join(j[2:])) <= 60:
            year += 1
    num += month * month * year
print(num)