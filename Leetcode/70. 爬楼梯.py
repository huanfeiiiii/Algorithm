# _*_ coding:utf-8 _*_

history = {}


def count(num):
    if num in history:
        return history[num]
    if num == 2:
        return 2
    if num == 1:
        return 1
    history[num] = count(num - 1) + count(num - 2)
    return count(num - 1) + count(num - 2)


print(count(100))
