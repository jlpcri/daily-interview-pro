from collections import defaultdict


def singleNumber(nums):
    count = defaultdict(int)   # initialize a dict, when call the dict it will auto add if key not exist

    for i in range(len(nums)):
        count[nums[i]] += 1    # count the appearance from nums

    print(nums)
    print(count)
    for i in range(len(nums)):
        if count[i] == 1:
            return i

    return False


s = [4, 3, 2, 4, 1, 3, 2]
print(singleNumber(s))