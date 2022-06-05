# _*_ coding:utf-8 _*_

n = int(input())
m = int(input())-1
d1 = {}
for i in range(1, n+1):
    d1[i] = sum([int(j) for j in str(i)])
print(sorted(d1.items(), key=lambda x: x[1])[m][0])