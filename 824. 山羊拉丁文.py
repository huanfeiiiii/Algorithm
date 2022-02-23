# _*_ coding:utf-8 _*_

sentence = "The quick brown fox jumped over the lazy dog"

l1 = sentence.split(' ')
l2 = []
s1 = 'a e i o u'
for num, data in enumerate(l1):
    data = list(data)
    if data[0].lower() in s1:
        data.append('ma')
    else:
        first = data.pop(0)
        data.append(first)
        data.append('ma')
    data.append('a'*(num+1))
    l2.append(''.join(data))
print(l2)