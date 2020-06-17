global maximum


def find_lis_recursive(nums):
    # allow access of global var
    global maximum
    # initial value
    maximum = 1

    count = find_lis_recursive_helper(nums, len(nums))

    return count


def find_lis_recursive_helper(arr, n):
    # allow access of global var
    global maximum
    # base case
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    max_ending_here = 1

    # Recursively get all LIS ending with arr[0] ... arr[n-2]
    for i in range(1, n):
        res = find_lis_recursive_helper(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > max_ending_here:
            max_ending_here = res + 1

    # compare maxEndingHere with overall maximum
    maximum = max(maximum, max_ending_here)

    return max_ending_here


def find_lis_dynamically(nums):
    n = len(nums)

    # result array
    result = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and result[i] < result[j] + 1:
                result[i] = result[j] + 1

    return max(result)


n = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
n1 = [10, 22, 9, 33, 21, 50, 41, 60]
print(find_lis_dynamically(n))
# 6, [0, 2, 6, 9 , 11, 15]

print(find_lis_dynamically(n1))
# 5,