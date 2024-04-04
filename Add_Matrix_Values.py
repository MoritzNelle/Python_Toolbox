'''
READ ME:
- This module contains the function add_matrices()

DESCRIPTION:
- The function add_matrices performs element-wise addition of two matrices.
- It first checks if the two matrices have identical dimensions. If not, it raises a ValueError.
- It then creates a new matrix with the same dimensions as the input matrices.
- It performs element-wise addition of the two matrices and stores the result in the new matrix.
- The function returns the new matrix.

PARAMETERS:
- matrix1: a list of lists, where each inner list represents a row of the matrix.
- matrix2: a list of lists, where each inner list represents a row of the matrix.

LIMITATIONS:
- The function only works with matrices of identical dimensions.
- The function does not handle cases where the matrices contain non-numeric values.
- The function does not handle cases where the matrices are not properly formed (i.e., rows have different lengths).

STRUCTURES:
- An if-statement is used to check if the dimensions of the two matrices are identical.
- Two nested for-loops are used to perform the element-wise addition of the two matrices.

OUTPUT:
- The function returns a new matrix that is the result of the element-wise addition of the two input matrices.
'''

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]): # Check if matrices have identical dimensions
        raise ValueError("Matrices must have identical dimensions")

    result = []

    for i in range(len(matrix1)): # Perform element-by-element addition
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# Example usage
matrix1 = [[ 35,12,  6],[-32, 5,-26],[10, 8, -1]]
matrix2 = [[-31,29,-34],[ 12,11,-25],[28,21,-42]]
result = add_matrices(matrix1, matrix2)
print(result)