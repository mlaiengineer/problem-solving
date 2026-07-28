def diagonalDifference(arr):
    # Store the sums of the two diagonals.
    left_right_diagonal = right_left_diagonal = 0

    # Loop through each row using its index.
    for i in range(len(arr)):
        # Used only to adjust the column index for each diagonal.
        counter = 0

        # Primary diagonal: row index == column index (0,0), (1,1), ...
        left_right_diagonal += arr[i][i]


        # Secondary diagonal: uses negative indexing to access rows
        # from the bottom while moving across columns.
        right_left_diagonal += arr[-i][i - 1]

    # Find the difference between the two diagonal sums.
    result = left_right_diagonal - right_left_diagonal

    # Return the absolute value of the difference.
    return -result if result < 0 else result