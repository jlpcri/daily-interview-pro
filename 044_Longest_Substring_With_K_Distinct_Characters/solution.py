MAX_CHARS = 26


def isValid(count, k):
    '''
    Calculate number of unique characters using a associative array count[]
    Returns true if number of uniq chars less than required k
    else returns false
    :param count:
    :param k:
    :return:
    '''
    val = 0
    for i in range(MAX_CHARS):
        if count[i] > 0:
            val += 1

    return k >= val


def longest_substring_with_k_distinct_characters(s, k):
    '''
    Find the maximum substring with exactly k unique characters
    :param s:
    :param k:
    :return:
    '''
    u = 0  # number of unique chars
    n = len(s)

    # Associative array to store the count of each char
    count = [0] * MAX_CHARS

    for i in range(n):
        if count[ord(s[i]) - ord('a')] == 0:
            u += 1

        count[ord(s[i]) - ord('a')] += 1

    # If there are not enough unique chars return error
    if u < k:
        return 'Not Enough unique characters'

    # Take a window with first element in it, start and end variable
    curr_start = 0
    curr_end = 0

    # Initialize values for result longest window
    max_window_size = 1
    max_window_start = 0

    # ReInitialize associative array
    count = [0] * MAX_CHARS

    # Put the first char
    count[ord(s[0]) - ord('a')] += 1

    for i in range(1, n):
        count[ord(s[i]) - ord('a')] += 1
        curr_end += 1

        # if there are more than k unique chars in current window,
        # remove from left side
        while not isValid(count, k):
            count[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1

        # update the max window size if required
        if curr_end - curr_start + 1 > max_window_size:
            max_window_size = curr_end - curr_start + 1
            max_window_start = curr_start

    return max_window_size, s[max_window_start: max_window_start + max_window_size]


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
print(longest_substring_with_k_distinct_characters('aabacbebebe', 3))
# 7 ()