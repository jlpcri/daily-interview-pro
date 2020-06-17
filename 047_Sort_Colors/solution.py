class Solution:
    def __init__(self):
        self.red = 0
        self.white = 1
        self.blue = 2

    def sortColors(self, nums):
        count_red = nums.count(self.red)
        count_white = nums.count(self.white)
        count_blue = nums.count(self.blue)

        for i in range(count_red):
            nums[i] = self.red

        for i in range(count_red, count_red + count_white):
            nums[i] = self.white

        for i in range(count_red + count_white, count_red + count_white + count_blue):
            nums[i] = self.blue

        return nums


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
Solution().sortColors(nums)
print("After Sort: ")
print(nums)