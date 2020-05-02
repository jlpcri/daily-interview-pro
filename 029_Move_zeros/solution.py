class Solution():
    def moveZero(self, nums):
        '''
        Traverse nums, put non zero num from the head of list
        through another counter count_non_zero
        Fill remains of list all zero
        :param nums:
        :return:
        '''
        count_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count_non_zero] = nums[i]
                count_non_zero += 1

        for i in range(count_non_zero, len(nums)):
            nums[i] = 0

        return nums


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print(nums)
Solution().moveZero(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

nums = [0, 1, 0, 3, 12]
print(nums)
Solution().moveZero(nums)
print(nums)
# [1,3,12,0,0]