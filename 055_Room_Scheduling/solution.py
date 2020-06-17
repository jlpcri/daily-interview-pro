MAX = 100001


def min_rooms(lectures):
    '''
    Time T start with 0, need to find the maximum of ongoing lectures at t, then find maximum number of lectures
    prefix_sum array stores the number of lectures ongoing at time t
    :param lectures:
    :return:
    '''
    # array to store the number of lectures ongoing at time t
    prefix_sum = [0] * MAX

    # for each lecture increment start point s
    # decrement endpoint (t + 1)
    for i in range(len(lectures)):
        prefix_sum[lectures[i][0]] += 1    # start time t
        prefix_sum[lectures[i][1] + 1] -= 1   # end time e

    # print(prefix_sum)
    # ans = prefix_sum[0]
    # loop prefix sum and update ans
    for i in range(1, MAX):
        prefix_sum[i] += prefix_sum[i - 1]
        # ans = max(ans, prefix_sum[i])

    return max(prefix_sum)


l = [(30, 75), (0, 50), (60, 150)]
# l = [(0, 5), (1, 2), (1, 10)]
print(min_rooms(l))
# 2