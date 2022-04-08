# _*_ coding:utf-8 _*_


def isValid(s):
    left = '({['
    d1 = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for i in s:
        if i in left:
            stack.append(d1[i])
        else:
            if not stack:
                return False
            else:
                if i == stack[-1]:
                    stack.pop()
                else:
                    return False
    return stack == []


n = "()[]{}"
print(isValid(n))
