# -*- coding:utf-8 -*-

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d1 = {}
for i in strs:
    src = ''.join(sorted(list(i)))
    if src in d1:
        d1[src].append(i)
    else:
        d1[src] = [i]

print(list(d1.values()))
