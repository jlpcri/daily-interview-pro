class Solution:
    def reverse(self, x):
        if x > 2**31 - 1 or x < -2**31:
            return 0
        if x > 0:
            return int(str(x)[::-1])
        if x < 0:
            return -1 * int(str(abs(x))[::-1])


n1 = -12300
n2 = 2**31
print(Solution().reverse(n1))
# 321
print(Solution().reverse(n2))
# 0
