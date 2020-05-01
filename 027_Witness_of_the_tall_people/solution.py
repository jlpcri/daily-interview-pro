def witnesses(heights):
    # Fill this in.
    max_height = 0
    count = 0
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > max_height:
            count += 1
            max_height = heights[i]

    return count


print(witnesses([3, 6, 3, 4, 1]))
# 3