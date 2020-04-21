def check(arr):
    # Fill in
    count = 0
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            count += 1
        if count > 1:
            return False

    return True


# s = [13, 4, 7]
s = [5, 1, 3, 2, 5]
print(check(s))