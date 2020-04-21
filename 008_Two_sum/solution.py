def two_sum(list, k):
    # Fill this in.
    result = False
    visited = set()
    for num in list:
        diff = k - num
        print(visited)
        if diff in visited:
            result = True
            break
        else:
            visited.add(num)

    return result

input = [6, 7, 11, 15, 3, 6, 5, 3]
k = 4

# input = [4, 7, 1, -3, 2]
# k = 5
print(two_sum(input, k))
# True
