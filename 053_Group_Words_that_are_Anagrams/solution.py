from _collections import defaultdict


def group_anagram_words(strs):
    arr = []
    result = defaultdict(list)

    for str in strs:
        key = ''.join(sorted(str))
        result[key].append(str)

    for item in result.values():
        arr.append(item)

    return arr


s = ['abc', 'bcd', 'cba', 'cbd', 'efg']
print(group_anagram_words(s))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
