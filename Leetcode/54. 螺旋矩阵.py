# _*_ coding:utf-8 _*_

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = []

while matrix:
    ans.extend(matrix[0])
    matrix = list(zip(*matrix[1:]))[::-1]
    print(matrix)
print(ans)
