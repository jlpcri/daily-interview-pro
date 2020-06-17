def isSorted(words, order):
    order_idx = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for k in range(min(len(word1), len(word2))):
            if word1[k] != word2[k]:
                if order_idx[word1[k]] > order_idx[word2[k]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False

    return True


w1 = ['abcd', 'efgh']
o1 = 'zyxwvutsrqponmlkjihgfedcba'
w2 = ["zyx", "zyxw", "zyxwy"]
o2 = 'zyxwvutsrqponmlkjihgfedcba'
w3 = ["hello", "leetcode"]
o3 = 'habcldefgijkmnopqrstuvwxyz'

print(isSorted(w1, o1))
# False
print(isSorted(w2, o2))
# True
print(isSorted(w3, o3))
# True
