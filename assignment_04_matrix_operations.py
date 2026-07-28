# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if rows > 0 else 0
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    if cols_a != rows_b:
        raise ValueError("Number of columns in A must equal number of rows in B.")

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            sum_product = 0
            for k in range(cols_a):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(sum_product)
        result.append(new_row)
    return result
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                row = list(map(int, row_input.split()))
                if len(row) != cols:
                    print(f"Error: You must enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid integers separated by spaces.")
    return matrix
if __name__ == "__main__":
    # Part A: Transpose a Matrix
    print("Part A: Transpose a Matrix")
    rows_a = int(input("Enter number of rows: "))
    cols_a = int(input("Enter number of columns: "))
    matrix_a = read_matrix(rows_a, cols_a)
    transposed_a = transpose_matrix(matrix_a)
    print("\nOriginal Matrix:")
    for row in matrix_a:
        print(" ".join(map(str, row)))
    print("\nTransposed Matrix:")
    for row in transposed_a:
        print(" ".join(map(str, row)))

    # Part B: Add Two Matrices
    print("\nPart B: Add Two Matrices")
    rows_b = int(input("Enter number of rows for both matrices: "))
    cols_b = int(input("Enter number of columns for both matrices: "))
    print("Matrix A:")
    matrix_b1 = read_matrix(rows_b, cols_b)
    print("Matrix B:")
    matrix_b2 = read_matrix(rows_b, cols_b)
    sum_matrix = add_matrices(matrix_b1, matrix_b2)
    print("\nSum of Matrices:")
    for row in sum_matrix:
        print(" ".join(map(str, row)))

    # Part C: Multiply Two Matrices
    print("\nPart C: Multiply Two Matrices")
    rows_c1 = int(input("Enter number of rows for Matrix A: "))
    cols_c1 = int(input("Enter number of columns for Matrix A (and rows for Matrix B): "))
    rows_c2 = cols_c1  # Number of rows in B must equal number of columns in A
    cols_c2 = int(input("Enter number of columns for Matrix B: "))