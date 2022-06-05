# _*_ coding:utf-8 _*_

s = "leetcode"
wordDict = ["leet", "code"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
n = len(s)
dp = [False] * (n + 1)
dp[0] = True
for i in range(n):
    for j in range(i + 1, n + 1):
        print(dp, i, j)
        if dp[i] and (s[i:j] in wordDict):
            dp[j] = True

