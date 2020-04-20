class Solution:
    def isValid(self, s):
        # Fill in this
        stack = []
        parenthese = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in parenthese.values():
                stack.append(i)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                else:
                    return False

                if x == parenthese[i]:
                    pass
                else:
                    return False

        print(stack)
        return False if stack else True


s = ['()(){()()', '', '([{}])()', '{[]{()}}', '[{}{})(]', '())(()']

for item in s:
    print(item, '-', Solution().isValid(item))