def max_subarray_sum(arr):
    max_so_far = arr[0]
    current_max = arr[0]

    print(arr)
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        max_so_far = max(max_so_far, current_max)
        print(arr[i], '*', current_max, '*', max_so_far)

    return max_so_far


def max_subarray_sum_with_index(arr):
    max_so_far = -10000000
    current_max = 0
    start = 0
    end = 0
    s = 0

    i: int
    for i in range(len(arr)):
        current_max += arr[i]

        if max_so_far < current_max:
            max_so_far = current_max
            start = s
            end = i

        if current_max < 0:
            current_max = 0
            s = i + 1

    return [max_so_far, arr[start:end + 1]]


# arr = [34, -50, 42, 14, -5, 86]   # 137
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]   # 7
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]    # -3
print(max_subarray_sum_with_index(arr))
# 137 2:6