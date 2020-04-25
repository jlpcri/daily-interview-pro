def distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    # result = editDistance(s1, s2, len_s1, len_s2)
    result = editDistDP(s1, s2, len_s1, len_s2)
    return result


def editDistance(s1, s2, len_s1, len_s2):
    if len_s1 == 0:
        return len_s2

    if len_s2 == 0:
        return len_s1

    if s1[len_s1 - 1] == s2[len_s2 - 1]:
        return editDistance(s1, s2, len_s1 - 1 , len_s2 - 1)

    return 1 + min(
        editDistance(s1, s2, len_s1, len_s2 - 1),      # insert
        editDistance(s1, s2, len_s1 - 1, len_s2),      # remove
        editDistance(s1, s2, len_s1 - 1, len_s2 - 1)   # replace
    )


def editDistDP(s1, s2, len_s1, len_s2):
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],     # insert
                    dp[i - 1][j],     # remove
                    dp[i - 1][j - 1]  # replace
                )

    # print(dp)
    return dp[len_s1][len_s2]


s1 = [
    ["biting", "sitting"],
    ['geek', 'gesek'],
    ['cut', 'catt'],
    ['sunday', 'saturday']

]

for item in s1:
    print(distance(item[0], item[1]))