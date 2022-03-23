# _*_ coding:utf-8 _*_

nums = [2,0,2,1,1,0]
n = 0
for i in range(nums.count(0)):
    nums.remove(0)
    n += 1
nums = [0]*n + nums
print(nums)
for i in range(nums.count(2)):
    nums.remove(2)
    nums.append(2)
print(nums)
