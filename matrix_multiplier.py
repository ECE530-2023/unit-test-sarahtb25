import numpy as np
'''
1. Get user inputs for 2 matrices
2. Check if number of columns of first matrix == number of rows of second matrix
3. Check if there are any non-integer or non-float values given
'''


def matrix_multiplier(first_matrix, second_matrix):
    # print(first_matrix)
    # print()
    # print(second_matrix)

    result = check_matrices(first_matrix, second_matrix)

    if (result == "OK"):
        return np.dot(first_matrix, second_matrix)

    return result


def check_matrices(first_matrix, second_matrix):
    check_dimensions_of_matrices = check_dimensions(
        first_matrix, second_matrix)

    if (check_dimensions_of_matrices != "OK"):
        return check_dimensions_of_matrices

    check_values_first_matrix = check_matrix_for_non_integer_values(
        first_matrix)

    if (check_values_first_matrix != "OK"):
        return check_values_first_matrix

    check_values_second_matrix = check_matrix_for_non_integer_values(
        second_matrix)

    if (check_values_second_matrix != "OK"):
        return check_values_second_matrix

    return "OK"


def check_dimensions(first_matrix, second_matrix):
    is_first_matrix_empty = check_empty_matrix(first_matrix)
    if is_first_matrix_empty:
        return "Empty matrix!"

    is_second_matrix_empty = check_empty_matrix(second_matrix)
    if is_second_matrix_empty:
        return "Empty matrix!"

    first_number_of_columns = len(first_matrix[0])
    second_number_of_rows = len(second_matrix)
    if (first_number_of_columns != second_number_of_rows):
        return "Number of columns of first matrix does not match number of rows of second matrix!"

    return "OK"


def check_matrix_for_non_integer_values(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if not (isinstance(matrix[row][column], int) or isinstance(matrix[row][column], float)):
                return "Non-integer value given!"

    return "OK"


def check_empty_matrix(matrix):
    if len(matrix[0]) == 0:
        return True

    return False
