from random import randint


def print_matrix(matrix, columns, rows):
    for j in range(0, columns):
        row = ''
        for i in range(0, rows):
            cell = matrix[i][j]
            cell_format: any = f'{cell: >4},'
            row = row + cell_format
        print(row)


def generate_matrix(rows, columns):
    Magic = [[randint(-10, 10) for i in range(1, rows+1)] for j in range(1, columns+1)]
    return(Magic)


def matrix_control_of_null_rows_and_columns(matrix, rows, columns):
    print('\n')
    print("\033[34m {}\033[0m".format(' - *' * 10))
    k = 0  # Finding the number of zeros in matrix cells
    rows_with_zeros = []
    columns_with_zeros = []
    for j in range(0, columns):
        for i in range(0, rows):
            if matrix[i][j] == k:
                rows_with_zeros.append(i)  # memorizing row with zero
                columns_with_zeros.append(j)
                print("\033[37m {}\033[0m".format(f'- zero cell of the matrix -'))
                print(f'row-{j}, column-{i} - this is the zero cell')
            continue
    if len(rows_with_zeros) + len(columns_with_zeros) == 0:
        print("\033[33m {}\033[0m".format(" There are no zero cells in the Matrix"))
    else:
        zero_cells(matrix, rows, columns, rows_with_zeros, columns_with_zeros)


def zero_cells(matrix, rows, columns, rows_with_zeros, columns_with_zeros):
    for j in range(0, columns):
        for i in range(0, rows):
            if j in columns_with_zeros or i in rows_with_zeros:
                matrix[i][j] = 0


def main():
    a = int(input('   Enter the number rows: '))
    b = int(input('Enter the number columns: '))
    rows, columns = a, b
    print("\033[34m {}\033[0m".format(' - *' * 10))
    print('\n')
    print("\033[35m {}\033[0m".format("   - Original matrix -"))
    Magic = generate_matrix(rows, columns)
    print_matrix(Magic, rows=rows, columns=columns)
    matrix_control_of_null_rows_and_columns(matrix=Magic, rows=rows, columns=columns)
    print_matrix(Magic, rows=rows, columns=columns)



main()
