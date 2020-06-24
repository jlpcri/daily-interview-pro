def find_range(nums):
    '''
    1. Find the candidate unsorted subarray
        a. scan from left to right and find the first element which is greater than the next element
        b. scan from right to left and find the first element which is smaller than next
    2. check whether sorting the candidate unsorted subarray makes the complete array sorted or not
        a. find the minimum and maximum of unsorted subarray
        b. find the first element in array[0: start - 1] which is greater than minimum, update start
        c. find the first element in array[n - 1: end] which is smaller than maximum, update end
    :param nums:
    :return:
    '''
    n = len(nums)
    start, end = 0, 0

    for i in range(n - 2):
        if nums[i] > nums[i + 1]:
            start = i
            break
    if start == n - 1:
        return 'The complete array is sorted'

    for i in range(n - 1, -1, -1):
        if nums[i] < nums[i - 1]:
            end = i
            break

    max_ele = max(nums[start: end + 1])
    min_ele = min(nums[start: end + 1])

    for i in range(start):
        if nums[i] > min_ele:
            start = i
            break

    for i in range(n - 1, end, -1):
        if nums[i] < max_ele:
            end = i
            break

    return start, end


s1 = [1, 7, 9, 5, 7, 8, 10]
s2 = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
s3 = [0, 1, 15, 25, 6, 7, 30, 40, 50]
print(find_range(s1))
# (1, 5)
print(find_range(s2))
# (3, 8)
print(find_range(s3))
# (2, 5)
