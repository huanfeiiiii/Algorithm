# _*_ coding:utf-8 _*_

nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]

# nums = [3, 2, 1, 0, 4]
right = len(nums) - 1
while right >= 0:
    if len(nums) - right < nums[right]:
        end = nums[-1]
    else:
        end = nums[right + nums[right]]
    if end != 0:
        for i in range(right, right + nums[right]):
            try:
                nums[i] = True
            except IndexError:
                break
    else:
        for i in range(right, right + nums[right] - 1):
            try:
                nums[i] = True
            except IndexError:
                break
    right -= 1
print(nums, all(nums))
