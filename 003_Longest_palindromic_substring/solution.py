# Assumption: a palindrome is any string that has length >= 2
class Solution:
    def longestPalindrome(self, s):
        # Fill in this
        palindrome = []

        for i in range(len(s)):
            for j in range(i + 2, len(s)):  # because of Assumption we put j from i+2
                tmp = s[i: j + 1]
                if tmp == tmp[::-1]:
                    palindrome.append(tmp)

        result = max(palindrome, key=len) if palindrome else None

        # print(palindrome)
        # print(result)
        return result


s = "tracecars"
# s = "aba"
print(str(Solution().longestPalindrome(s)))
