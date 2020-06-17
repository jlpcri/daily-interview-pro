def find_ranges(nums):
    result = []
    start = end = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            result.append('{0}->{1}'.format(start, end))
            start = nums[i]
            end = nums[i]
        else:
            end = nums[i]

    result.append('{0}->{1}'.format(start, end))
    return result


n = [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
print(find_ranges(n))
# ['0->2', '5->5', '7->11', '15->15']
