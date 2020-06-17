class Solution:
    def reverse_words(self, str):
        result = ''
        words = str.split(' ')
        for word in words:
            result += word[::-1] + ' '

        result = result.rstrip()
        return result


s = 'The cat in the hat'
print(Solution().reverse_words(s))
# ehT tac ni eht tah
