# -*- coding:utf-8 -*-

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = list(paragraph.lower())
for i in range(len(paragraph)):
    if not (97 <= ord(paragraph[i]) <= 122 or ord(paragraph[i]) == 32):
        paragraph[i] = ' '
paragraph = [i for i in ''.join(paragraph).split(' ') if i]

d1 = {}
for i in paragraph:
    if i not in banned:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
print(sorted(d1.items(), key=lambda x: x[1])[-1][0])
