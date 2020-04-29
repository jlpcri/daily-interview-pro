class Solution:
    def minSubArrayLen(self, nums, s):
        # Fill this in
        subarray_pair = []
        subarray_lengh = []
        start = end = 0
        for i in range(len(nums)):
            start = i
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp >= s:
                    end = j
                    subarray_pair.append((start, end))
                    subarray_lengh.append(end - start + 1)
                    break

        print(subarray_pair)
        print(subarray_lengh)
        return min(subarray_lengh) if subarray_lengh else 0


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2