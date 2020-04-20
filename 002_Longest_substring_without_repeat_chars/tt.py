class Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        appeared_chars = dict()
        start = end = 0
        substring_start_end = []
        substring_length = []

        for i, currentChar in enumerate(s):
            if currentChar not in appeared_chars:
                appeared_chars[currentChar] = i
                end = i
            else:
                if currentChar == s[i-1]:
                    start = i
                    end = i
                    appeared_chars.clear()
                    appeared_chars[currentChar] = i
                else:
                    start = appeared_chars[currentChar] + 1
                    end = i
                    appeared_chars = {k: v for k, v in appeared_chars.items() if v >= start}
                    appeared_chars[currentChar] = i

            print(appeared_chars)
            substring_start_end.append((start, end))
            substring_length.append(end - start + 1)

        print(substring_start_end)
        print(substring_length)
        for i in substring_start_end:
            print(s[i[0]: i[1] + 1])

        return max(substring_length) if substring_length else 0


sample_string = 'abcdb'
# sample_string = 'abrkaabcdefghijjxxx'
print(Solution().lengthOfLongestSubstring(sample_string))
# 10
