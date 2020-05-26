def countNthSay(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'

    # Find n'th term by generating all terms from 3 to n-1

    # Initialize previouse term
    previous_term = '11'
    for i in range(3, n + 1):
        # Because previous character is processed in current iteration
        # we add a dummy character to make sure that loop runs one extra iteration
        previous_term += '$'

        count = 1  # Initialize count of matching chars
        tmp = ''   # Initialize i'th term in series

        # process previous term to find the next term
        for j in range(1, len(previous_term)):
            # if current char not equal previous
            if previous_term[j] != previous_term[j - 1]:
                # append count of str[j - 1] to tmp
                tmp += str(count)

                # Append str[j-1]
                tmp += previous_term[j - 1]

                # reset count
                count = 1
            else:
                count += 1

        previous_term = tmp

    return previous_term


for i in range(1, 10):
    print(i, countNthSay(i))