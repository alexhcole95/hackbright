def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    if not matrix:
        return

    number_of_rows = len(matrix)
    number_of_cols = len(matrix[0])

    positions_to_clear = []

    for row_num in range(number_of_rows):
        for col_num in range(number_of_cols):
            if matrix[row_num][col_num] == 0:
                print(f'Found a zero in row: {row_num}, col: {col_num}')

                positions_to_clear.append((row_num, col_num))

    for (row_num, col_num) in positions_to_clear:
        # zero out the row
        for j in range(number_of_cols):
            matrix[row_num][j] = 0

        # zero out the column
        for i in range(number_of_rows):
            matrix[i][col_num] = 0

    return matrix


print('Actual:', zero_matrix([
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 0, 'H'],
    ['I', 'J', 'K', 'L']
]))

print('Expected:', [['A', 'B', 0, 'D'], [0, 0, 0, 0], ['I', 'J', 0, 'L']])
