import sympy as sp

def row_echelon(matrix):
    matrix = sp.Matrix(matrix)
    rref_matrix, pivot_columns = matrix.rref()
    return rref_matrix.tolist(), pivot_columns

#INPUT
matrix = [[10, 88],
          [35, 129]]

echelon_matrix, pivot_columns = row_echelon(matrix)
print("The row Echelon form is: ")
for row in echelon_matrix:
    print(row)

def matrix_rank(matrix):
    matrix = sp.Matrix(matrix)
    rank = matrix.rank()
    return rank

rank = matrix_rank(matrix)
print("The rank of the matrix is: ", rank)
