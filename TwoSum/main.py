def sum(nums, target):
    _nums = {}
    length = len(nums)

    for i in range(length):
        value = target - nums[i]
        if value in _nums:
            return [_nums[value], i]
        _nums[nums[i]] = i

nums = [3,7,4,1,8,2]
target = 15
result = sum(nums, target)
print(result)