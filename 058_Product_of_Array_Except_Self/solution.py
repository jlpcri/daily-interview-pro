def products(nums):
    '''

    :param nums:
    :return:
    '''
    # Base case
    nums_len = len(nums)
    if nums_len == 1:
        print(0)
        return

    # products array
    result = [1] * nums_len
    i, tmp = 1, 1

    # After the loop, product array contains product of
    # elements on left side except self
    for i in range(nums_len):
        result[i] = tmp
        tmp *= nums[i]

    tmp = 1

    # After loop, product contains product of
    # elements on left and right except self
    for i in range(nums_len - 1, -1, -1):
        result[i] *= tmp
        tmp *= nums[i]

    return result


n = [1, 2, 3, 4, 5]
n1 = [10, 3, 5, 6, 2]

print(products(n))
# [120, 60, 40, 30, 24]
print(products(n1))
# [180, 600, 360, 300, 900]
