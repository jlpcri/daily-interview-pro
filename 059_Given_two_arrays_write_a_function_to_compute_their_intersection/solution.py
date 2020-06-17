class Solution:
    def intersection1(self, num1, num2):
        return list(set(num1) & set(num2))

    def intersection2(self, num1, num2):
        return list(set(num1).intersection(num2))

    def intersection(self, num1, num2):
        return list(set([value for value in num1 if value in num2]))


s = [[4, 9, 5], [9, 4, 9, 8, 4]]
s1 = [[1, 2, 2, 1], [2, 2]]
print(Solution().intersection(s1[0], s1[1]))
# [2]
print(Solution().intersection(s[0], s[1]))
# [9, 4]
