# _*_ coding:utf-8 _*_

def compressString(S):
    """
    :type S: str
    :rtype: str
    """
    i = 0
    j = 1
    ls = len(S)
    s = ''
    while i < ls:
        while j < ls and S[i] == S[j]:
            j += 1
        s += S[i] + str(j - i)
        i = j
    if len(s) < len(S):
        return s
    else:
        return S


print(compressString("abbccd"))
