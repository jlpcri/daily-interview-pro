
def matrix_spiral_print(matrix):
    '''
    k - starting row index
    m - ending row index
    l - starting col index
    n - ending col index
    i - iterator
    :param matrix:
    :return:
    '''

    k = 0
    m = len(matrix)

    l = 0
    n = len(matrix[0])

    while k < m and l < n:
        # print the first row from remaining rows
        for i in range(l, n):
            print(matrix[k][i], end=' ')
        k += 1  # remove first row

        # print the last col from remaining cols
        for i in range(k, m):
            print(matrix[i][n - 1], end=' ')
        n -= 1  # remove last col

        # print the last row from remaining rows
        if k < m:
            for i in range(n - 1, l - 1, -1):
                print(matrix[m - 1][i], end=' ')
            m -= 1  # remove last row

        # print the first col from remaining cols
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(matrix[i][l], end=' ')
            l += 1  # remove first col

    print()


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

grid = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]
matrix_spiral_print(grid)
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
matrix_spiral_print(grid)
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10