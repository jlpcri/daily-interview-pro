def merge(intervals):
    '''
    1) Sort all intervals in decreasing order of start time.
    2) Traverse sorted intervals starting from first interval,
       do following for every interval.
       a) If current interval is not first interval and it
         overlaps with previous interval, then merge it with
         previous interval. Keep doing it while the interval
         overlaps with the previous one.
       b) Else add current interval to output list of intervals
    :param intervals:
    :return:
    '''
    # Fill this in.
    # sort intervals based on the increasing order of the start interval
    intervals.sort(key=lambda x: x[0])
    # print(intervals)

    # Array to hold the merged intervals
    result = []
    start = -10000
    end = -100000

    for i in range(len(intervals)):
        a = intervals[i]
        if a[0] > end:
            if i != 0:
                result.append((start, end))
            end = a[1]
            start = a[0]
        else:
            if a[1] >= end:
                end = a[1]

        # 'end' value gives the end point of that particular interval
        # 'start' gives the start point of that interval
        # 'result' array contains the list of all merged intervals

    if end != -100000 and (start, end) not in result:
        result.append((start, end))

    return result


print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]

print(merge([(6, 8), (1, 9), (2, 4), (4, 7)]))
# [(1, 9)]