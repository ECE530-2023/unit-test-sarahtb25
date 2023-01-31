def matrix_multiplier(first_matrix, second_matrix):
    '''
    Calls function to check if the matrices are valid.
    If valid, does the matrix multiplication.
    '''
    # print(first_matrix)
    # print()
    # print(second_matrix)

    check_matrices(first_matrix, second_matrix)

    # Matrix multiplication done here
    number_of_rows_of_first_matrix = len(first_matrix)
    number_of_columns_of_second_matrix = len(second_matrix[0])
    answer = [[0 for i in range(number_of_columns_of_second_matrix)]
              for j in range(number_of_rows_of_first_matrix)]

    # iterate through rows of first_matrix
    for i in range(len(first_matrix)):
        # iterate through columns of second_matrix
        for j in range(len(second_matrix[0])):
            # iterate through rows of second_matrix
            for k in range(len(second_matrix)):
                answer[i][j] += first_matrix[i][k] * second_matrix[k][j]

    return answer


def check_matrices(first_matrix, second_matrix):
    '''
    Calls function to check if dimensions of matrices are valid.
    If valid, calls function to check if there are any non-integer or non-float values.
    '''
    # Check dimensions of matrices
    check_dimensions(first_matrix, second_matrix)

    # Check if there are any non-integer or non-float values
    check_matrix_for_non_integer_or_float_values(first_matrix)
    check_matrix_for_non_integer_or_float_values(second_matrix)


def check_dimensions(first_matrix, second_matrix):
    '''
    Calls function to check if there are any empty rows in the matrix.
    If all is fine, checks if the number of columns of the first matrix == number of rows of the second matrix
    '''
    # Check if there are any empty rows in the matrices
    check_empty_row_in_matrix(first_matrix)
    check_empty_row_in_matrix(second_matrix)

    # Checks if the number of columns of the first matrix == number of rows of the second matrix
    first_number_of_columns = len(first_matrix[0])
    second_number_of_rows = len(second_matrix)
    if (first_number_of_columns != second_number_of_rows):
        raise ValueError(
            "Number of columns of first matrix does not match number of rows of second matrix!")


def check_empty_row_in_matrix(matrix):
    '''
    Checks if the matrix is empty or if it has any empty rows
    '''
    if len(matrix) == 1 and len(matrix[0]) == 0:
        raise ValueError("Empty matrix!")
    else:
        base_length_of_row = len(matrix[0])

        for row in range(len(matrix)):
            if len(matrix[row]) != base_length_of_row:
                raise ValueError("Length of rows in matrix are not equal!")


def check_matrix_for_non_integer_or_float_values(matrix):
    '''
    Checks if any value in the matrix is a non-integer or non-float value
    '''
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if not (isinstance(matrix[row][column], int) or isinstance(matrix[row][column], float)):
                raise ValueError("Non-integer value given!")
