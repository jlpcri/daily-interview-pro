def word_search(matrix, word):
    # Fill this in.
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        word_ = ''.join(matrix[row])
        print(word_)
        if word_ and word in word_:
            return True

    for col in range(cols):
        word_ = ''
        for row in range(rows):
            word_ += matrix[row][col]
        print(word_)
        if word_ and word in word_:
            return True

    return False

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
target = 'FOBM'
# target = 'OBQP'
print(word_search(matrix, target))
# True