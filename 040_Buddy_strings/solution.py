class Solution:
    def buddyStrings(self, A, B):
        '''
        1. Check if both strings have equal length
        2. Compare both strings and count number of unmatched characters
           and store the index of unmatched characters
        3. If unmatched chars more than 2 then return False
        4. If unmatched chars only 1 then return False
        4. Check if on swapping two chars both strings are identical
           then return True
        5. Otherwise, return False
        '''
        len1 = len(A)
        len2 = len(B)

        if len1 != len2:
            return False

        # Store indexes of previously mismatched characters
        previous = -1
        current = -1

        # number of mismatched chars
        count = 0

        # index of array
        i = 0
        while i < len1:
            if A[i] != B[i]:
                count += 1

                if count > 2:
                    return False

                previous = current
                current = i

            i += 1

        if count < 2:
            return False

        if A[previous] == B[current] and A[current] == B[previous]:
            return True
        else:
            return False


a = 'aaaaaaaaabc'
b = 'aaaaaaaaacb'
c = 'aaaaaaaabbc'

print(Solution().buddyStrings(a, b))  # True
print(Solution().buddyStrings(c, b))  # False
