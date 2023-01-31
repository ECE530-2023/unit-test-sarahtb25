import matrix_multiplier
import pytest


def test_non_integer_value_1():
    first_matrix = [['a', 1], [2, 3]]
    second_matrix = [[1, 2], [3, 4]]

    with pytest.raises(ValueError, match="Non-integer value given!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_rows_columns_mismatch_2():
    first_matrix = [[1, 2]]
    second_matrix = [[1, 2, 3]]

    with pytest.raises(ValueError, match="Number of columns of first matrix does not match number of rows of second matrix!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_first_matrix_empty_3():
    first_matrix = [[]]
    second_matrix = [[1, 2]]

    with pytest.raises(ValueError, match="Empty matrix!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_first_matrix_empty_4():
    first_matrix = [[]]
    second_matrix = [[1]]

    with pytest.raises(ValueError, match="Empty matrix!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_second_matrix_empty_5():
    first_matrix = [[1, 2]]
    second_matrix = [[]]

    with pytest.raises(ValueError, match="Empty matrix!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_lengths_of_matrices_mismatch_6():
    first_matrix = [[1, 2], [], [2, 3]]
    second_matrix = [[1, 2], [3, 5]]

    with pytest.raises(ValueError, match="Length of rows in matrix are not equal!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_lengths_of_matrices_mismatch_7():
    first_matrix = [[1, 2], [[1]], [2, 3]]
    second_matrix = [[1, 2], [3, 5]]

    with pytest.raises(ValueError, match="Length of rows in matrix are not equal!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_lengths_of_matrices_mismatch_8():
    first_matrix = [[], [[1]], [2, 3]]
    second_matrix = [[1, 2], [3, 5]]

    with pytest.raises(ValueError, match="Length of rows in matrix are not equal!"):
        matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)


def test_matrix_multiplication_9():
    first_matrix = [[1, 2], [3, 4]]
    second_matrix = [[5, 6, 7], [8, 9, 10]]

    assert matrix_multiplier.matrix_multiplier(
        first_matrix, second_matrix) == [[21, 24, 27], [47, 54, 61]]


def test_matrix_multiplication_10():
    first_matrix = [[1, 0.5]]
    second_matrix = [[2, 4], [6, 8]]

    assert matrix_multiplier.matrix_multiplier(
        first_matrix, second_matrix) == [[5, 8]]
