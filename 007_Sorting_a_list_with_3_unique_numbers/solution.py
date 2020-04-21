def sortNums(nums):
    # mergeSort/quickSort etc best performance O(n log n)
    # O(n) countingSort/radixSort

    countArr = [0 for _ in range(3)]   # [0, 0, 0]
    sortArr = []

    for i in nums:
        countArr[i - 1] += 1   # i = 1, 2, 3

    print(countArr)
    for i in range(3):
        for j in range(countArr[i]):
            sortArr.extend([i + 1])

    return sortArr

nums = [3, 3, 2, 1, 3, 2, 1]
print(sortNums(nums))