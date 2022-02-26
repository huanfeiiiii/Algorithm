# _*_ coding:utf-8 _*_
word1 = "abcdeef"
word2 = "abaaacc"
word1.lower()
word2.lower()
for i in range(97, 123):
    if abs(word1.count(chr(i)) - word2.count(chr(i))) > 3:
        print(False)
        # exit()
print(True)