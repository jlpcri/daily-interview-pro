import bisect


def running_median(stream):
    result = []
    arr_sort = []

    for idx, n in enumerate(stream):
        if idx == 0:
            result.append(n)
            arr_sort.append(n)
        elif idx % 2 == 0:   # odd numbers of length
            insert_sorted_list(arr_sort, n)
            result.append(arr_sort[idx // 2])
        elif idx % 2 == 1:   # even numbers of length
            insert_sorted_list(arr_sort, n)
            m = (arr_sort[(idx + 1) // 2] + arr_sort[(idx+1) // 2 - 1]) / 2
            result.append(m)

    print(result)


def insert_sorted_list(arr, n):
    bisect.insort(arr, n)

    return arr


s = [2, 1, 4, 7, 2, 0, 5]
running_median(s)
# 2 1.5 2 3.0 2 2.0 2
