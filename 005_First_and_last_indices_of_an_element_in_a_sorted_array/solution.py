class Solution:
    def getRange(self, arr, target):
        # Fill in this
        index = self.binary_search(arr, target)
        if index == -1:
            return [-1, -1]

        left = right = index

        while left - 1 >= 0 and arr[left - 1] == target:
            left -= 1

        while right + 1 < len(arr) and arr[right + 1] == target:
            right += 1

        return [left, right]

    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            midpoint = (low + high) // 2   #  5 / 2 = 2.5, 5 // 2 = 2
            # midpoint = int(midpoint)

            # print(low, midpoint, high)

            if arr[midpoint] == target:
                return midpoint
            elif arr[midpoint] < target:
                low = midpoint + 1
            else:
                high = midpoint - 1

        return -1


# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# x = 2

# arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
# x = 9

# arr = [100, 150, 150, 153]
# x = 150

# arr = [1, 2, 3, 4, 5, 6, 10]
# x = 9

arr = [2, 3, 5, 8, 10]
x = 1
print(Solution().getRange(arr, x))

data = {
    '2': [1, 2, 2, 2, 2, 3, 4, 7, 8, 8],
    '9': [1, 3, 3, 5, 7, 8, 9, 9, 9, 15],
    '150': [100, 150, 150, 153],
    '8': [1, 2, 3, 4, 5, 6, 10]
}

for k in data:
    print(Solution().getRange(data[k], int(k)))