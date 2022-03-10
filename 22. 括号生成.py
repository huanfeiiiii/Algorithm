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


def generateParenthesis2(n):
    l1 = ['']
    while l1[0].count('(') < n:
        temp = l1.pop(0)
        for i in range(len(temp) + 1):
            in_temp = list(temp)
            in_temp.insert(i, '()')
            in_temp = ''.join(in_temp)
            if in_temp not in l1:
                l1.append(in_temp)
    return l1


print(generateParenthesis2(3))
