import collections


class Window:
    def __init__(self):
        self.count = collections.Counter()  # counts of such number
        self.nonzero = 0                    # counts of distinct numbers

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1


class Solution(object):
    def findSequence(self, A, K):
        window1 = Window()
        window2 = Window()
        max_length = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:    # window1 points the given subarray has (<= k) distinct numbers
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:   # window2 points the given subarray has (< k) distinct numbers
                window2.remove(A[left2])
                left2 += 1

            if left2 - left1 + 1 > max_length:  # update max_length if it's greater than max_length
                max_length = left2 - left1 + 1

            print(A[left1:left2 + 1])

        return max_length


seq = [1, 3, 5, 3, 1, 3, 1, 5]
k = 2
# seq = [1, 2, 1, 2, 3]
# k = 2
# seq = [1, 2, 1, 3, 4]
# k = 3
print('res: ', Solution().findSequence(seq, k))
