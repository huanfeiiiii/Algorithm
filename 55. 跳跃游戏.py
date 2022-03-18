# _*_ coding:utf-8 _*_

nums = [1,0,2]

l1 = list(range(1, nums[0] + 1))
print(l1)
l2 = []
while max(l1) < len(nums) - 1:
    for i in l1:
        l2.extend(list(range(i + 1, nums[i] + i + 1)))
    if list(set(l2)) == l1:
        print(False)
        exit()
    l1 = list(set(l2))
print(True)
