from diagonal_difference import diagonalDifference

def run_test():
    # HackerRank sample
    assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15, 'Test case 1 failed'

    # 1x1 matrix (both diagonals are the same element)
    assert diagonalDifference([[5]]) == 0, 'Test case 2 failed'

    # 2x2 matrix
    assert diagonalDifference([[1, 2], [3, 4]]) == 0, 'Test case 3 failed'

    # Equal diagonal sums
    assert diagonalDifference([[3, 2, 3],
                               [4, 5, 6],
                               [3, 8, 3]]) == 0, 'Test case 4 failed'

    # Matrix with negative numbers
    assert diagonalDifference([[-1, -2, -3],
                               [-4, -5, -6],
                               [-7, -8, -9]]) == 0, 'Test case 5 failed'

    # 4x4 matrix
    assert diagonalDifference([[1, 2, 3, 4],
                               [5, 6, 7, 8],
                               [9, 10, 11, 12],
                               [13, 14, 15, 16]]) == 0, 'Test case 6 failed'

    print('Passed all test cases')


if __name__ == '__main__':
    run_test()