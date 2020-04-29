class Solution():

    def num_ways(self, rows, cols):
        '''
        Using recursive solution to count number of ways
        to reach matrix[rows-1][cols-1] from matrix[0][0]
        The approach has exponential time complexity
        :param rows:
        :param cols:
        :return:
        '''

        # first row or first column return 1
        if rows == 1 or cols == 1:
            return 1

        # recursively find the number of ways to reach the current cell
        # sum of the ways of left cell and top cell
        return self.num_ways(rows - 1, cols) + self.num_ways(rows, cols - 1)

    def num_ways_dp(self, rows, cols):
        '''
        Dynamical Programming to resolve overlapping sub-problems
        Time complexity: O(rows * cols)
        :param rows:
        :param cols:
        :return:
        '''

        # Array to store sub-results
        paths = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    paths[row][col] = 1
                else:
                    paths[row][col] = paths[row - 1][col] + paths[row][col - 1]

        return paths[rows - 1][cols - 1]


n = 4
m = 3
print(Solution().num_ways_dp(n, m))
# 2

for i in range(1, 10):
    print(i, ': ', Solution().num_ways_dp(i, i + 2))