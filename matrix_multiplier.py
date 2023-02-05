import logging


def matrix_multiplier(first_matrix, second_matrix):
    '''
    Calls function to check if the matrices are valid.
    If valid, does the matrix multiplication.
    '''
    logging.basicConfig(filename='example.log', filemode='w',
                        level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('First Matrix: %s', first_matrix)
    logging.info('Second Matrix: %s', second_matrix)
    # print(first_matrix)
    # print()
    # print(second_matrix)

    result = check_matrices(first_matrix, second_matrix)

    # Matrix multiplication done here
    if (result == "OK"):
        logging.info('Both matrices ok, doing matrix multiplication')
        number_of_rows_of_first_matrix = len(first_matrix)
        number_of_columns_of_second_matrix = len(second_matrix[0])
        answer = [[0 for _ in range(number_of_columns_of_second_matrix)]
                  for _ in range(number_of_rows_of_first_matrix)]

        # iterate through rows of first_matrix
        for i in range(len(first_matrix)):
            # iterate through columns of second_matrix
            for j in range(len(second_matrix[0])):
                # iterate through rows of second_matrix
                for k in range(len(second_matrix)):
                    answer[i][j] += first_matrix[i][k] * second_matrix[k][j]

        logging.info('Matrix Multiplication = %s', answer)
        return answer

    return result


def check_matrices(first_matrix, second_matrix):
    '''
    Calls function to check if dimensions of matrices are valid.
    If valid, calls function to check if there are any non-integer or non-float values.
    '''
    # Check dimensions of matrices
    check_dimensions_of_matrices = check_dimensions(
        first_matrix, second_matrix)

    if (check_dimensions_of_matrices != "OK"):
        return check_dimensions_of_matrices

    # Check if there are any non-integer or non-float values
    check_values_first_matrix = check_matrix_for_non_integer_or_float_values(
        first_matrix)

    if (check_values_first_matrix != "OK"):
        return check_values_first_matrix

    check_values_second_matrix = check_matrix_for_non_integer_or_float_values(
        second_matrix)

    if (check_values_second_matrix != "OK"):
        return check_values_second_matrix

    return "OK"


def check_dimensions(first_matrix, second_matrix):
    '''
    Calls function to check if there are any empty rows in the matrix.
    If all is fine, checks if the number of columns of the first matrix == number of rows of the second matrix
    '''
    # Check if there are any empty rows in the matrices
    check_empty_row = check_empty_row_in_matrix(first_matrix)
    if check_empty_row != "OK":
        return check_empty_row

    check_empty_row = check_empty_row_in_matrix(second_matrix)
    if check_empty_row != "OK":
        return check_empty_row

    # Checks if the number of columns of the first matrix == number of rows of the second matrix
    first_number_of_columns = len(first_matrix[0])
    second_number_of_rows = len(second_matrix)
    if (first_number_of_columns != second_number_of_rows):
        logging.error(
            'Number of columns of first matrix %s does not match number of rows of second matrix %s', first_matrix, second_matrix)
        return "Number of columns of first matrix does not match number of rows of second matrix!"

    logging.info(
        'Number of columns of first matrix matches number of rows of second matrix')
    return "OK"


def check_empty_row_in_matrix(matrix):
    '''
    Checks if the matrix is empty or if it has any empty rows
    '''
    if len(matrix) == 1 and len(matrix[0]) == 0:
        logging.error('Empty matrix: %s', matrix)
        return "Empty matrix!"
    else:
        base_length_of_row = len(matrix[0])

        for row in range(len(matrix)):
            if len(matrix[row]) != base_length_of_row:
                logging.error(
                    'Length of rows in matrix %s are not equal!', matrix)
                return "Length of rows in matrix are not equal!"

    logging.info('Matrix %s does not have empty rows', matrix)
    return "OK"


def check_matrix_for_non_integer_or_float_values(matrix):
    '''
    Checks if any value in the matrix is a non-integer or non-float value
    '''
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if not (isinstance(matrix[row][column], int) or isinstance(matrix[row][column], float)):
                logging.error('Non-integer value given in matrix %s', matrix)
                return "Non-integer value given!"

    logging.info('Matrix %s contains only integer or float values', matrix)
    return "OK"
