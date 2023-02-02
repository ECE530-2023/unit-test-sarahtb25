import matrix_multiplier
import cProfile

known_cases = (([['a', 1], [2, 3]], [[1, 2], [3, 4]], "Non-integer value given!"),
               ([[1, 2]], [[
                1, 2, 3]], "Number of columns of first matrix does not match number of rows of second matrix!"),
               ([[]], [[1, 2]], "Empty matrix!"),
               ([[1, 2]], [
                []], "Empty matrix!"),
               ([[]], [[1]], "Empty matrix!"),
               ([[1, 2], [], [2, 3]], [[1, 2], [3, 5]],
                "Length of rows in matrix are not equal!"),
               ([[1, 2], [[1]], [2, 3]], [[1, 2], [3, 5]],
                "Length of rows in matrix are not equal!"),
               ([[], [[1]], [2, 3]], [[1, 2], [3, 5]],
                "Length of rows in matrix are not equal!"),
               ([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]],
                [[21, 24, 27], [47, 54, 61]]),
               ([[1, 0.5]], [[2, 4], [6, 8]], [[5, 8]]))


def test_matrix_multiplier():
    for first_matrix, second_matrix, expected_result in known_cases:
        result = matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)
        # print(result)

        assert expected_result == result


if __name__ == '__main__':
    cProfile.run('test_matrix_multiplier()')
    # test_matrix_multiplier()
