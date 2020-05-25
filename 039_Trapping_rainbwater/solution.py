def capacity1(arr):
    '''
    Approach: Traverse each element and find the highest bar on left and right.
              Take the smaller of left/right highest.
              the difference between the smaller height and current element
              is the amount of the water that can be stored in current element
    Algorithm:
        1. Traverse the array from start to end
        2. For each element, find left highest bar(a) and right highest bar(b)
        3. Add (min(a, b) - current) to the result
    '''
    result = 0

    for i in range(1, len(arr)):
        # Find maximum element of left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find maximum element of right
        right = arr[i]
        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])

        # Update the amount of trapping rainwater
        result += min(left, right) - arr[i]

    return result


def capacity(arr):
    '''
    Efficient approach to the above solution
    Pre-calculate highest left and right of each element
    Store into two array
    Update trapping rainwater
    '''
    n = len(arr)
    # left[i] contains height of highest bar to the left of current ith element
    # include itself
    left = [0] * n

    # right[i] contains highest bar to the right of current
    right = [0] * n

    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    # Fill right array
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    result = 0
    for i in range(n):
        result += min(left[i], right[i]) - arr[i]

    return result


nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]   # 6
nums1 = [2, 0, 2]  # 2
nums2 = [3, 0, 2, 0, 4]  # 7
print(capacity(nums))
# 6
print(capacity(nums1))
print(capacity(nums2))