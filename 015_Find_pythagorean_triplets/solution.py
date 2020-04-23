def findPythagoreanTriplets(nums):
    nums_length = len(nums)
    nums = sorted(nums)
    for i in range(nums_length):
        nums[i] = nums[i] * nums[i]

    for i in range(nums_length - 1, 1, -1):    # pointer i from end to start
        left = 0
        right = i - 1
        while left < right:
            sum_of_two = nums[left] + nums[right]
            if sum_of_two == nums[i]:
                return True
            elif sum_of_two < nums[i]:
                left += 1
            else:
                right -= 1

    return False


s = [3, 5, 12, 5, 13]
print(findPythagoreanTriplets(s))