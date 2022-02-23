# _*_ coding:utf-8 _*_


def generateParenthesis(n: int) -> list:
    l1 = ['']
    while True:
        temp = l1.pop(0)
        l2 = [temp + '(', temp + ')']
        for i in l2:
            if i.count(')') > i.count('(') or i.count('(') > n:
                l2.remove(i)
        l1.extend(l2)
        if min([i.count(')') for i in l1]) == n:
            return l1

