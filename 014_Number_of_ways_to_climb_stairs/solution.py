# Recursion with Memoization
# Time: O(n), Size of recursion tree can go upto n
# Space: O(n), The depth of recursion tree can go upto n
def staircase(n):
    cache = [0] * n * 2
    cache[0] = 1
    cache[1] = 1

    result = staircase_(n, cache)
    print(cache)
    return result


def staircase_(n, cache):
    if n <= 1:
        return cache[n]
    else:
        cache[n] = staircase_(n - 2, cache) + staircase_(n - 1, cache)
        return cache[n]


# Dynamical Programming
def staircase_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    if n <= 1:
        return dp[n]
    else:
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

    print(dp)
    return dp[n]

# print(staircase(4))
n = 40
# print(staircase(n))
print(staircase_dp(n))