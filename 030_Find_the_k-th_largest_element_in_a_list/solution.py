import heapq


def findKthLargest(nums, k):
    '''
    The property of this data structure in python is that
    each time the smallest of heap element is popped(min heap).
    Whenever elements are pushed or popped,
    heap structure in maintained.
    The heap[0] element also returns the smallest element each time
    :param nums:
    :param k:
    :return:
    '''
    # define a heap which always store largest kth nums
    # if length of result is greater than k, then pop the minimum
    result = []

    for i in range(len(nums)):
        heapq.heappush(result, nums[i])
        if len(result) > k:
            heapq.heappop(result)

    # print(result)
    return heapq.heappop(result)


print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5

print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
# 5

print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
# 4