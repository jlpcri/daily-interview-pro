class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 1):
            # initial left and right
            left = i + 1
            right = len(nums) - 1
            x = nums[i]

            while left < right:
                if x + nums[left] + nums[right] == 0:
                    result.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif x + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return result


n1 = [1, -2, 1, 0, 5]
n2 = [0, -1, 2, -3, 1]

print(Solution().threeSum(n1))
# [[-2, 1, 1]]
print(Solution().threeSum(n2))
# [[0, -1, 1], [2, -3, 1]]
