# _*_ coding:utf-8 _*_

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

left, right = [height[0]]*len(height), [height[-1]]*len(height)

for i in range(1, len(height)):
    left[i] = max(left[i-1], height[i-1])
for i in list(range(len(height)-1)[::-1]):
    right[i] = max(right[i+1], height[i+1])

print(sum([max(min(left[i], right[i])-height[i], 0) for i in range(len(height))]))
