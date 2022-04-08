# _*_ coding:utf-8 _*_

m = 3
n = 7

history = {}


def count(num):
    if tuple(num) in history:
        return history[tuple(num)]
    if num == [0, 1] or num == [1, 0] or num[0] == 0 or num[1] == 0:
        return 1
    else:
        history[tuple(num)] = count([num[0] - 1, num[1]]) + count([num[0], num[1] - 1])
        print(history)
        return count([num[0] - 1, num[1]]) + count([num[0], num[1] - 1])


print(count([m - 1, n - 1]))
