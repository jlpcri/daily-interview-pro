def get_bonuses(performance):
    n = len(performance)
    if n == 0:
        return
    if n == 1:
        return performance
    if n == 2:
        return [1, 2] if performance[0] < performance[1] else [2, 1]

    result = [1] * n
    updated = [False] * n
    for i in range(1, n):
        if performance[i - 1] < performance[i] and not updated[i]:
            if performance[i] < performance[i + 1]:
                result[i] += 1
            else:
                result[i] += 2

            updated[i] = True
        else:
            if not updated[i - 1]:
                result[i - 1] += 1
                updated[i - 1] = True

    return result


s = [1, 2, 3, 2, 3, 5, 1]
print(get_bonuses(s))
# 1, 2, 3, 1, 2, 3, 1
