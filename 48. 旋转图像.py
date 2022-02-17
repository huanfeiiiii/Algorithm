# -*- coding:utf-8 -*-
# 已解决

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 镜像
for i in matrix:
    m_right, m_left = 0, len(i) - 1
    while m_right < m_left:
        i[m_right], i[m_left] = i[m_left], i[m_right]
        m_right += 1
        m_left -= 1
# 对角转化
for i in range(len(matrix) - 1):
    right, left = [i, 0], [len(matrix) - 1, len(matrix[-1]) - 1]
    left[1] = left[1] - right[0]
    while right[1] < left[1]:
        left[0] = len(matrix[-1]) - 1 - right[1]
        matrix[right[0]][right[1]], matrix[left[0]][left[1]] = matrix[left[0]][left[1]], matrix[right[0]][right[1]]
        right[1] += 1
print(matrix)

