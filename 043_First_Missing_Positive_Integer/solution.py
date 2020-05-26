def first_missing_positive(nums):
    maximum = max(nums)
    if maximum < 1:
        return 1

    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1

    l = [0] * maximum

    for i in range(len(nums)):
        if nums[i] > 0:
            if l[nums[i] - 1] != 1:
                l[nums[i] - 1] = 1

    for i in range(len(l)):
        if l[i] == 0:
            return i + 1

    return maximum + 1


nums = [
    [3, 4, -2, 1],                 # 2
    [0, 10, 2, -10, -20],          # 1
    [2, 3, 7, 6, 8, -1, -10, 15],  # 1
    [2, 3, -7, 6, 8, 1, -10, 15],  # 4
    [1, 1, 0, -1, -2]              # 2
]
for item in nums:
    print(first_missing_positive(item))
# 2