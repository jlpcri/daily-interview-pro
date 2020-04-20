class Solution:
    def lengthOfLognestSubstring(self, s):
        # Fill this in
        non_repeat_string = dict()
        start = 0
        end = 0
        seqPair = []
        seqLength = []

        for i, currentChar in enumerate(s):
            if currentChar not in non_repeat_string:
                non_repeat_string[currentChar] = i
                end = i
            else:
                if currentChar == s[i - 1]:  # 'abcdd'
                    start = i
                    end = i
                    non_repeat_string.clear()
                    non_repeat_string[currentChar] = i
                else:
                    start = non_repeat_string[currentChar] + 1
                    end = i
                    non_repeat_string = {k: v for k, v in non_repeat_string.items() if v >= start}  # remove unnecessary records ?
                    non_repeat_string[currentChar] = i

            print(non_repeat_string)
            seqPair.append((start, end))
            seqLength.append(end - start + 1)

        print( seqPair)
        print(seqLength)
        for i in seqPair:
            print(s[i[0]: i[1] + 1])
        return max(seqLength) if seqLength else 0

sample_string = 'abrkaabcdefghijjxxx'
# sample_string = 'abcdb'
print(Solution().lengthOfLognestSubstring(sample_string))